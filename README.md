# SELCAL

## Basic overview
Aircraft traveling in remote areas such as oceans communicate with air traffic control (ATC) using high frequency (HF) radio, rather than the very high frequency radios used for communication in more trafficked areas.  This is because HF radio has a longer range, but comes with the drawback that there is typically more noise.  Aircrews using HF for communication traditionally needed to listed to this noisy frequency continuously, in case controllers contacted them.

SELCAL is a system by which each aircraft is assigned a four character alphanumeric code.  When a controller wishes to speak with the aircrew, they transmit the aircraft's code encoded as a sound.  The aircraft's HF radio is turned on and listening, but with the volume turned down so the pilots don't need to listen.  When the aircraft's radio hears its code, it alerts the pilots to turn up the volume and call the controller back.

## Code rules
The original system is called SELCAL 16 and used 16 letters between A and S, excluding the letters I, N, and O.  SELCAL 32 is an expansion, adding the letters T through Z and the numerals 1 through 9.  Code assignments follow the following two rules:
* a character must never be repeated
* the first character of each pair must be the alphanumerically lower one (i.e. A before F, 3 before 8)

## Audio encoding
![400](https://asri.aero/wp-content/uploads/2022/01/SELCAL-Code-Blocks-1.jpeg)
This example is for the code AC-BD.

Each character is assigned a unique frequency.  The first two characters are transmitted simultaneously for one second, followed by a 0.2 second gap, then the final two characters for one second.