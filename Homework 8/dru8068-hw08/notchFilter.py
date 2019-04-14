"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""
import numpy as np
import matplotlib.pyplot as plt

def applyNotch(fs, dataFile) :
    f = 17
    w = 2 * np.pi * f / fs
    data = np.genfromtxt(dataFile, delimiter=",")
    y = np.array([])
    print(len(data))
    for n in range(0,len(data) + 100):
        y = np.append(y, y_n(n,w,data,y))

    plt.figure()
    plt.title("Original Signal")
    plt.plot(data)
    plt.xlim(-25,625)
    plt.figure()
    plt.title("Filtered Signal")
    plt.plot(y)
    plt.ylim(-2.25,2.25)
    plt.figure()
    plt.title("10 Hz Signal Combined w/ 33 Hz Signal")
    x = np.arange(fs)
    y_1 = np.sin(2 * np.pi * 10 * x / fs)
    y_2 = np.sin(2 * np.pi * 33 * x / fs)
    total = y_1 + y_2
    plt.plot(x,total)
    plt.xlim(-25,625)

    plt.show()
    

def y_n(n,w,data,y):
    if n < 0:
        return 0
    if n < len(y-1):
        return y[n]
    j = np.complex(0,1)
    value = 0.9372 * 2 * np.cos(w) * y_n(n-1,w,data,y) - 0.8783 * y_n(n-2,w,data,y) + x_n(n,data) - 2 * np.cos(w) * x_n(n - 1, data) + x_n(n - 2, data)
    return value

def x_n(n, data):
    if n < 0 or n > len(data) - 1:
        return 0
    return data[n]


############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
