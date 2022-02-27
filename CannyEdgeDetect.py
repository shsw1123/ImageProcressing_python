import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread("Figures/GreenScreenSuperman.jpg")
image = cv2.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Original",image)
# "Canny" computed canny edge detection algoithm
canny10 = cv.Canny(image, 10, 250)
canny50 = cv.Canny(image,50,250)
canny100 = cv.Canny(image,100,250)
canny200  = cv.Canny(image,200,250)

plt.subplot(221),plt.imshow(canny10,"gray"), plt.title("Canny-LowThres=10")
plt.subplot(222),plt.imshow(canny50,"gray"), plt.title("Canny-LowThres=50")
plt.subplot(223),plt.imshow(canny100,"gray"), plt.title("Canny-LowThres=100")
plt.subplot(224),plt.imshow(canny200,"gray"), plt.title("Canny-LowThres=200")
plt.show()
cv.waitKey(0)
