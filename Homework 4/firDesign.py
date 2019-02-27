"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""
import numpy as np
import matplotlib.pyplot as plt
"""
    Low Pass Filter portion start
"""
cutoffFrequency = 50
filterLength = 21
filterOrder = filterLength - 1
samplingFrequency = 2000
transitionFrequency = cutoffFrequency / samplingFrequency
w = np.array([])

data = open("data-filtering.csv")
string_data = data.readline()
string_data = string_data.split(",")

float_data = np.array([])
for x in string_data:
    float_data = np.append(float_data,np.array([float(x)]))

n = 0
while n < filterLength:
    if n == filterOrder / 2:
        w = np.append(w, 2 * transitionFrequency)
    else:
        w = np.append(w, np.sin(2 * np.pi * transitionFrequency * (n - (filterOrder / 2))) / (np.pi * (n - filterOrder/2)))
    n = n + 1

lowpassFiltered = np.convolve(w, float_data)
"""
    End Low Pass Filter portion
"""
"""
    Start High Pass Filter portion
"""
cutoffFrequency_High = 280
filterLength_High = 21
filterOrder_High = filterLength_High - 1
transitionFrequency_High = cutoffFrequency_High / samplingFrequency
w_High = np.array([])

n = 0
while n < filterLength:
    if n == filterOrder / 2:
        w_High = np.append(w_High, 1 - 2 * transitionFrequency_High)
    else:
        w_High = np.append(w_High, -1 * np.sin(2 * np.pi * transitionFrequency_High * (n - (filterOrder_High/2))) / (np.pi * (n - (filterOrder_High / 2))))
    n = n + 1

firstHundred = float_data[0:100]

highpassFiltered = np.convolve(w_High, firstHundred)
highpassFiltered = highpassFiltered[0:100]
"""
    End High Pass Filter portion
"""
"""
    Plotting for Low Pass Filter
"""
x = np.arange(0,2000,1)
phase = 2 * np.pi * 4 * 0.01
y = np.cos(2 * np.pi * 4 * x/samplingFrequency) 

plt.figure(1)
plt.subplots_adjust(hspace = 0.75)

plt.subplot(311)
plt.plot(float_data)
plt.title("original signal")

plt.subplot(312)
plt.plot(x,y)
plt.title("4 Hz signal")

plt.subplot(313)
plt.plot(lowpassFiltered)
plt.title("application of low pass filter")

plt.show()

"""
    Plotting for High Pass Filter
"""
x_High = np.arange(0,100,1)
phase_High = 2 * np.pi * 330 * 0.01
y_High = np.cos(2 * np.pi * 330 * x_High/samplingFrequency)

plt.figure(2)
plt.subplots_adjust(hspace = 0.75)

plt.subplot(311)
plt.plot(firstHundred)
plt.title("original signal")

plt.subplot(312)
plt.plot(x_High,y_High)
plt.title("330 Hz signal")

plt.subplot(313)
plt.plot(highpassFiltered)
plt.title("application of high pass filter")

plt.show()
