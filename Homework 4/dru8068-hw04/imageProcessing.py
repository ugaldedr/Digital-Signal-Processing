"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
"""
    Part a
"""

boat = mpimg.imread("boat.512.tiff")
clock = mpimg.imread("clock-5.1.12.tiff")
man = mpimg.imread("man-5.3.01.tiff")
tank = mpimg.imread("tank-7.1.07.tiff")

plt.figure()
plt.imshow(boat, cmap="gray")
plt.title("Boat")

plt.figure()
plt.imshow(clock, cmap="gray")
plt.title("Clock")

plt.figure()
plt.imshow(man, cmap="gray")
plt.title("Man")

plt.figure()
plt.imshow(tank, cmap="gray")
plt.title("Tank")

"""
    Part b
"""

h = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
LPFBoat = np.empty((0,521))

for line in boat:
    result = np.convolve(h,line)
    LPFBoat = np.append(LPFBoat, [result], axis=0)

plt.figure()
plt.imshow(LPFBoat, cmap="gray")
plt.title("LPF Boat")

LPFClock = np.empty((0,265))

for line in clock:
    result = np.convolve(h,line)
    LPFClock = np.append(LPFClock, [result], axis=0)

plt.figure()
plt.imshow(LPFClock, cmap="gray")
plt.title("LPF Clock")

LPFMan = np.empty((0,1033))

for line in man:
    result = np.convolve(h,line)
    LPFMan = np.append(LPFMan, [result], axis=0)

plt.figure()
plt.imshow(LPFMan, cmap="gray")
plt.title("LPF Man")

LPFTank = np.empty((0,521))

for line in tank:
    result = np.convolve(h,line)
    LPFTank = np.append(LPFTank, [result], axis=0)

plt.figure()
plt.imshow(LPFTank, cmap="gray")
plt.title("LPF Tank")

"""
   Part c
"""

c = np.array([1, -1])

HPFBoat = np.empty((0,513))

for line in boat:
    result = np.convolve(c,line)
    HPFBoat = np.append(HPFBoat, [result], axis=0)

plt.figure()
plt.imshow(HPFBoat, cmap="gray")
plt.title("HPF Boat")

HPFClock = np.empty((0,257))

for line in clock:
    result = np.convolve(c,line)
    HPFClock = np.append(HPFClock, [result], axis=0)

plt.figure()
plt.imshow(HPFClock, cmap="gray")
plt.title("HPF Clock")

HPFMan = np.empty((0,1025))

for line in man:
    result = np.convolve(c,line)
    HPFMan = np.append(HPFMan, [result], axis=0)

plt.figure()
plt.imshow(HPFMan, cmap="gray")
plt.title("HPF Man")

HPFTank = np.empty((0,513))

for line in tank:
    result = np.convolve(c,line)
    HPFTank = np.append(HPFTank, [result], axis=0)

plt.figure()
plt.imshow(HPFTank, cmap="gray")
plt.title("HPF Tank")

"""
    Part d
"""
darin = mpimg.imread("darinGrayNoise.jpg")

plt.figure()
plt.imshow(darin, cmap="gray")
plt.title("Noisy Darin")

LPFDarin = np.empty((0,649))

for line in darin:
    result = np.convolve(h,line)
    LPFDarin = np.append(LPFDarin, [result], axis=0)

plt.figure()
plt.imshow(LPFDarin, cmap="gray")
plt.title("LPF Darin")

median = ndimage.median_filter(darin, 5)

plt.figure()
plt.imshow(median, cmap="gray")
plt.title("Median Darin")

plt.show()
