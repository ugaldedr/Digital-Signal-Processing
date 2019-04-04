"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def plotting(FFT_OG, FFT_filtered):
    plt.figure(1)
    plt.subplot(121)
    plt.plot(FFT_filtered)
    plt.subplot(122)
    plt.plot(FFT_OG)
    plt.show()

def processFile(fn, offset):
    data, sampleRate = sf.read(fn)
    FFT = np.fft.fft(data)
    index = int(len(FFT) / 2 - 1)
    for x in range(index - offset - 1, index + offset):
        FFT[x] = 0
    IFFT = np.fft.ifft(FFT)
    IFFT = IFFT.real
    plotting(FFT, np.fft.fft(data))
    sf.write('cleanMusic.wav',IFFT,sampleRate)

##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 10000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
