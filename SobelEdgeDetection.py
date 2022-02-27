import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
image = cv.imread("Figures/BlueColor.jpg")
image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

sobelX = cv.Sobel(image,cv.CV_64F,1,0,3) # along x-axis with K-size = 3
sobelY = cv.Sobel(image,cv.CV_64F,0,1,3) # along y-axis with K-size = 3
# Convert trough (negative-derivative) and crest (positive-derivative) into absolute values
sobelX = np.uint8(np.abs(sobelX))
sobelY = np.uint8(np.abs(sobelY))
# "bitwise_and" calculates the per-element bit-wise conjunction of 2 array
sobelCombined = cv.bitwise_or(sobelX,sobelY)

plt.subplot(221),plt.imshow(image,"gray"),plt.title("original")
plt.subplot(222),plt.imshow(sobelX,"gray"),plt.title("SobelX")
plt.subplot(223),plt.imshow(sobelY,"gray"),plt.title("SobelY")
plt.subplot(224),plt.imshow(sobelCombined,"gray"),plt.title("SobelXY")
plt.show()