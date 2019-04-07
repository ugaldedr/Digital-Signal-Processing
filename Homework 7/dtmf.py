"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""
from scipy.signal import freqz
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


def processTones(name, L, fs, samplesPerTone):
    data = np.genfromtxt(name, delimiter=',')
    phone_number = ''
    x = 0
    while x < len(data):
        tone = data[x:x + 3999]
        phone_number = phone_number + str(bandpassFilter(L, fs, samplesPerTone, tone))
        x = x + 4000
    plotting(L, fs, samplesPerTone, data)
    return phone_number

        
def bandpassFilter(L, fs, samplesPerTone, tone):
    frequencies = np.array([697, 770, 852, 941, 1209, 1336, 1477])
    values = np.array([])
    for x in range(0,len(frequencies)):
        n = np.arange(0,L,1)
        h = np.array([])
        for y in range(0,L):
            h = np.append(h,2 / L * np.cos(2 * np.pi * frequencies[x] * n[y] / fs))
        y = np.convolve(tone,h)
        values = np.append(values, np.mean(y**2))
    one, two = two_largest(values)
    temp = 0
    if two > one:
        temp = one
        one = two
        two = temp
    return str(determineKey(int(one), int(two)))

def two_largest(values):
    largest = 0
    second_largest = 0
    largestLoc = 0
    secondLoc = 0
    for x in range(0,len(values)):
        if values[x] > largest:
            second_largest = largest
            secondLoc = largestLoc
            largest = values[x]
            largestLoc = x
        elif largest > values[x] > second_largest:
            secondLoc = x
            second_largest = values[x]
    return largestLoc, secondLoc

def determineKey(one, two):
    if one is 4 and two is 0:
        return '1'
    elif one is 4 and two is 1:
        return '4'
    elif one is 4 and two is 2:
        return '7'
    elif one is 4 and two is 3:
        return '*'
    elif one is 5 and two is 0:
        return '2'
    elif one is 5 and two is 1:
        return '5'
    elif one is 5 and two is 2:
        return '8'
    elif one is 5 and two is 3:
        return '0'
    elif one is 6 and two is 0:
        return '3'
    elif one is 6 and two is 1:
        return '6'
    elif one is 6 and two is 2:
        return '9'
    elif one is 6 and two is 3:
        return '#'

def plotting(L, fs, samplesPerTone, data):
    frequencies = np.array([697, 770, 852, 941, 1209, 1336, 1477])
    plt.figure()
    plt.title("Frequency Responses of Bandpass Filters")
    plt.xlabel("Hertz")
    for x in range(0,len(frequencies)):
        n = np.arange(0,L,1)
        h = np.array([])
        for y in range(0,L):
            h = np.append(h,2 / L * np.cos(2 * np.pi * frequencies[x] * n[y] / fs))
        i, j = freqz(h,1)
        plt.plot(i*1000,abs(j))
    plt.figure()
    f, t, Sxx = signal.spectrogram(data, fs)
    plt.pcolormesh(t, np.fft.fftshift(f), np.fft.fftshift(Sxx, axes=0))
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("time [sec]")
    plt.show()
        


#############  main  #############
if __name__ == "__main__":
    filename = "tones-123456789star0pound.csv"  # name of file to process
    L = 64                  # filter length
    fs = 8000               # sampling rate
    samplesPerTone = 4000   # 4000 samples per tone, 
                            # NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)
    
    print(phoneNumber)

