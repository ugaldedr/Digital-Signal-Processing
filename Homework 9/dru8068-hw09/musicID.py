"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob
from heapq import nsmallest

def classifyMusic() :
    songList = []
    data, sampleRate = sf.read('testSong.wav')
    signatureTable = {}
    for name in glob.glob('song-*.wav'):
        signature = getSignature(name)
        signatureTable[name] = signature
    f, t, Sxx = spectrogram(data, sampleRate, nperseg=sampleRate//2)
    testSignature = np.array([])
    for y in range(0,len(Sxx[0])):
        testSignature = np.append(testSignature,f[np.argmax(Sxx[:,y])])
    normTable = {}
    for x in signatureTable:
        check = getNorm(signatureTable[x],testSignature)
        normTable[x] = int(check)
    topFive = nsmallest(5, normTable, key=normTable.get)
    topTwo = nsmallest(2, normTable, key=normTable.get)
    for x in topFive:
        print(normTable.get(x),"",x)
    plotSpectrograms(topTwo, data, sampleRate)

def getSignature(fn):
    data, sampleRate = sf.read(fn)
    signature = np.array([])
    f, t, Sxx = spectrogram(data, sampleRate, nperseg=sampleRate//2)
    for y in range(0,len(Sxx[0])):
        signature = np.append(signature,f[np.argmax(Sxx[:,y])])
    return signature

def getNorm(s,t):
    return np.linalg.norm(s-t,1)

def plotSpectrograms(topTwo, data, sampleRate):
    for x in topTwo:
        plt.figure()
        data1, sampleRate1 = sf.read(x)
        plt.title(x)
        plt.specgram(data1, Fs=sampleRate1)
    plt.figure()
    plt.title("Test Song")
    plt.specgram(data, Fs=sampleRate)

    plt.show()


###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()
