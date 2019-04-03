"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 3313 Digital Signal Processing
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import data
from skimage.feature import match_template

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def findImage(mainImage, template) :
    erb = mpimg.imread(mainImage)
    segment = mpimg.imread(template)
    erbGray = rgb2gray(erb)
    segmentGray = rgb2gray(segment)
    plt.figure()
    plt.imshow(erbGray, cmap = "gray")
    plt.figure()
    plt.imshow(segmentGray, cmap = "gray")
    result = match_template(erbGray,segmentGray)
    row = np.argmax(np.max(result,axis=0))
    column = np.argmax(np.max(result,axis=1))
    print('The image appears to be at ('+ str(row) + ','+ str(column) + ')')
    for x in range(row,row + int(len(segmentGray))):
        for y in range(column,column + int(len(segmentGray[0]))):
            erbGray[y,x] = 0
    plt.figure()
    plt.imshow(erbGray, cmap = "gray")
    plt.show()
#############  main  #############
if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    findImage(mainImage, template)
