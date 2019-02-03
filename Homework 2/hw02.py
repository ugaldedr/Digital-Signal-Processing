"""
    Name: Dario Ugalde
    Mav ID: 1001268068
    Course: CSE 3313 Digital Signal Processing
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


halfNote = np.arange(0,0.5,0.000125) # half note sampled at 8000Hz 
notes = [52,52,59,59,61,61,59,59,57,57,56,56,54,54,56,52,59,59,57,57,56,56,54,54] # list of notes
TTLS = 0 # initializing variable to store song

for x in notes:
    frequency = 440 * 2 ** ((x - 49) / 12) # frequency calculation for each note
    note = np.cos(2 * np.pi * frequency * halfNote) # creating tone for each note
    TTLS = np.append(TTLS, note) # append tone

sf.write('twinkle.wav', TTLS, 8000) # create song
