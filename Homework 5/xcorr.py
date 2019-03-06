from scipy import signal as sig
import numpy as np

A = np.matrix([[1,0],[-1,2]])
B = np.matrix([[1,2,3],[-1,-2,-3]])

corr = sig.correlate2d(A,B)
print(corr)
