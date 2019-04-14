"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def plotting(data, y):
    FFT_data = np.abs(np.fft.fft(data))
    FFT_filter = np.abs(np.fft.fft(y))
    plt.figure()
    plt.title("Original Sound vs. Filtered Sound")
    plt.xlabel("Hertz")
    plt.subplot(121)
    plt.plot(FFT_data)
    plt.xlim(0,len(FFT_data)/4)
    plt.ylim(0,np.max(FFT_data))
    plt.subplot(122)
    plt.plot(FFT_filter)
    plt.xlim(0,len(FFT_data)/4)
    plt.ylim(0,np.max(FFT_data))
    plt.show()

def applyShelvingFilter(inName, outName, g, fc) :
    data, sampleRate = sf.read(inName)
    mu = 10**(g/20)
    theta_c = 2 * np.pi * fc / sampleRate
    gamma = (1 - (4 / (1 + mu)) * np.tan(theta_c / 2)) / (1 + (4 / (1 + mu))  * np.tan(theta_c / 2))
    alpha = (1 - gamma) / 2
    x1 = 0
    u1 = 0
    y = np.array([])
    for x in data:
        u = alpha * (x + x1) + gamma * u1
        x1 = x
        u1 = u
        y = np.append(y, u * (mu - 1) + x)
    plotting(data, y)
    sf.write(outName, y, sampleRate)


##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -20  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
