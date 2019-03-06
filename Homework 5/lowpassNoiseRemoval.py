"""
    Name:   Dario Ugalde
    Mav ID: 1001268068
    Course: CSE 3313 Digital Signal Processing
"""

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import freqz

"""
    Read wav file and set variables
"""

data, sampleRate = sf.read('P_9_2.wav')
cutoffFrequency = 7500
filterLength = 101
filterOrder = filterLength - 1
transitionFrequency = cutoffFrequency / sampleRate
h = np.array([])
w = np.array([])
h_hat = np.array([])

"""
    Create h[n] and w[n]
"""

n = 0
while n < filterLength:
    if n == filterOrder/2:
        h = np.append(h, 2 * transitionFrequency)
    else:
        h = np.append(h, np.sin(2 * np.pi * transitionFrequency * (n - (filterOrder / 2))) / (np.pi * (n - filterOrder/2)))

    w = np.append(w, 0.54 - (0.46 * np.cos(2 * np.pi * n / filterOrder)))
    n = n + 1

"""
    Apply Hamming Window to filter coefficients
"""

h_hat = np.multiply(h, w)
lowpassfiltered = np.convolve(h_hat, data)

"""
    Write filtered wav file and display frequency responses
"""

sf.write('cleanMusic.wav', lowpassfiltered, sampleRate)

i, j = freqz(h, 1)
x, y = freqz(h_hat, 1)

plt.figure()
plt.plot(i, abs(j))
plt.plot(x, abs(y))
plt.title("Frequency Response")
plt.show()
