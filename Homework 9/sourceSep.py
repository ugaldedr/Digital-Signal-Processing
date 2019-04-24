"""
   Name:   Dario ugalde
   MavID:  1001268068
   Course: CSE 3313 Digital Signal Processing

   Wed Nov  7 10:16:17 CST 2018

    given two audio files, each of which consists of a mixture
    of two audio sources, perform blind source separation
"""


import numpy as np
import soundfile as sf
from scipy import signal
from sklearn.decomposition import FastICA, PCA


def unmixAudio(leftName, rightName) :
    np.random.seed(0)
    s1, sampleRate1 = sf.read(leftName)
    s2, sampleRate2 = sf.read(rightName)

    S = np.c_[s1,s2]

    ica = FastICA(n_components=2)
    S_ = ica.fit_transform(S)
    
    out1 = S_[:,0]
    out1 = np.multiply(out1,10)
    out2 = S_[:,1]
    out2 = np.multiply(out2,10)

    sf.write('unmixed1.wav',out1,sampleRate1)
    sf.write('unmixed0.wav',out2,sampleRate2)

###################  main  ###################
if __name__ == "__main__" :
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
