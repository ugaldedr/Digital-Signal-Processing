import numpy as np
import cmath

x = np.array([1,2,1,2,0,0,0])
y = np.array([3,0,-1,-4,0,0,0])

x_dft = np.fft.fft(x)
y_dft = np.fft.fft(y)

Xz = np.multiply(x_dft,y_dft)

xz = np.fft.ifft(Xz)
print(xz)
