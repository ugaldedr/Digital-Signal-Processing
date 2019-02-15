"""
  Name: Dario Ugalde
   MavID: 1001268068
   Course: CSE 3313 Digital Signal Processing
"""

import numpy as np

values = open("data-communications.csv","r")
string_data = values.readline()
string_data = string_data.split(",")
float_data = 0
bits = 0
letter = 0
word = ""

for x in string_data:
   float_data = np.append(float_data,np.array([float(x)]))

pulse0 = np.ones(10)
pulse0 = pulse0 / np.linalg.norm(pulse0)
pulse1 = np.append(np.ones(5), -1 * np.ones(5))
pulse1 = pulse1 / np.linalg.norm(pulse1)

y = 1
while y < (len(float_data) - 1):
    pulse = float_data[y:y+10]
    pulse = pulse / np.linalg.norm(pulse)
    Cauchy_Schwartz_zero = abs(np.dot(pulse, pulse0) / (np.linalg.norm(pulse) * np.linalg.norm(pulse0)))
    Cauchy_Schwartz_one = abs(np.dot(pulse, pulse1) / (np.linalg.norm(pulse) * np.linalg.norm(pulse1)))
    if Cauchy_Schwartz_zero > Cauchy_Schwartz_one:
        bits = np.append(bits,np.array([0]))
    else:
        bits = np.append(bits,np.array([1]))
    y = y + 10

z = 1
while z < (len(bits) - 1):
    byte = bits[z:z+8]
    letter = byte[0] * 2**7 + byte[1] * 2**6 + byte[2] * 2**5 + byte[3] * 2**4 + byte[4] * 2**3 + byte[5] * 2**2 + byte[6] * 2**1 + byte[7] * 2**0
    word = word + chr(letter)
    z = z + 8

print(word)
