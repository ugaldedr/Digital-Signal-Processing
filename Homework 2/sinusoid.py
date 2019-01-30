import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-0.015,0.045,0.001)

frequency = 25
amplitude = 15
peakTime = 0.01
phase = 2 * np.pi * frequency * peakTime
print(phase)

y = amplitude * np.cos(2 * np.pi * frequency * x - phase)
plt.plot(x,y)
plt.grid()
plt.xlabel("time (seconds)")
plt.title("%d Hz signal with peak at t=%.2f" %(frequency,peakTime))

plt.show()