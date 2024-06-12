import json

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

if __name__ == '__main__':
    # check_valid('AC-BD')
    # check_valid('CA-BD')
    # check_valid('AABD')
    # check_valid('C9-BD')
    import doctest
    doctest.testmod()