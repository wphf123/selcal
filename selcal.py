import json
import sounddevice
import numpy as np
import time

with open('frequencies.json', 'r') as file:
    separated_freqs = json.load(file)

freqs = separated_freqs['SELCAL32']
limited_freqs = separated_freqs['SELCAL16']

letters = list(freqs.keys())
limited_letters = list(limited_freqs.keys())

def valid_code(code: str, allow_32: bool = True) -> bool:
    """Determines whether or not a provided code is valid according to
    SELCAL standards.  See readme.md for explanation of rules.
    
    Parameters
    ----------
    code
        The code to be evaluated.
    allow_32
        Whether or not to evaluate codes using the extended SELCAL 32
        character set as valid.  Default is True.

    Returns
    -------
    bool
        True if valid, False otherwise

    Examples
    --------
    >>> valid_code('AC-BD')
    True
    >>> valid_code('CA-BD')
    False
    >>> valid_code('AC-DB')
    False
    >>> valid_code('AABD')
    False
    >>> valid_code('C9-BD', False)
    False
    >>> valid_code('C9-BD')
    True
    """
    code_len = len(code)
    if code_len == 4 or code_len == 5:
        if code_len == 5:
            code = code[:2] + code[3:]
        if code.isalnum():
            if len(set(code)) == 4:
                if allow_32:
                    # there are faster but less readable ways of doing this
                    if all(c in letters for c in code):
                        if letters.index(code[0]) < letters.index(code[1]) \
                            and letters.index(code[2]) < letters.index(code[3]):
                            return True
                else:
                    if all(c in limited_letters for c in code):
                        if limited_letters.index(code[0]) < limited_letters.index(code[1]) \
                            and limited_letters.index(code[2]) < limited_letters.index(code[3]):
                            return True
    return False

def check_valid(code: str) -> None:
    """Convenience function for testing"""
    if valid_code(code, False):
        print(f'code {code} is a valid SELCAL 16 code')
    else:
        if valid_code(code, True):
            print(f'code {code} is a valid SELCAL 32 code only')
        else:
            print(f'code {code} is an invalid SELCAL code')

def normalize(a):
    """Normalizes an array so that all values are between 0 and 1.
    Needs to be done to the combined waveforms to prevent distortions"""
    return (a - np.min(a)) / (np.max(a) - np.min(a))

def tone(freq1: float, freq2: float) -> None:
    rate = 44100
    length = 1
    t = np.linspace(0, length, length * rate)
    waveform1 = np.sin(2 * np.pi * freq1 * t)
    waveform2 = np.sin(2 * np.pi * freq2 * t)
    combined_waveform = normalize(waveform1 + waveform2)
    sounddevice.play(combined_waveform, rate)
    sounddevice.wait()

def play_code(code: str) -> None:
    if len(code) == 5:
        code = code[:2] + code[3:]
    try:
        tone(freqs[code[0]], freqs[code[1]])
        time.sleep(0.2)
        tone(freqs[code[2]], freqs[code[3]])
    except KeyError:
        pass

if __name__ == '__main__':
    # check_valid('AC-BD')
    # check_valid('CA-BD')
    # check_valid('AABD')
    # check_valid('C9-BD')
    # import doctest
    # doctest.testmod()
    print('Enter codes below (type q or Ctrl-C to quit)')
    while True:
        try:
            code = input('> ')
        except KeyboardInterrupt:
            break
        if code == 'q':
            break
        code = code.upper()
        check_valid(code)
        play_code(code)