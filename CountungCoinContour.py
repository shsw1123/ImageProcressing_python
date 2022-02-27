import argparse

import cv2
import numpy as np
import cv2 as cv

image = cv.imread("Figures/Coins.jpg")
cv.imshow("Original",image)

image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(image,(7,7),0)
cv.imshow("Blurred",blurred)
# Canny
edge = cv.Canny(blurred,30,150)
cv.imshow("Edges",edge)

cnts, hierarchy = cv.findContours(edge,cv2.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

print("There are %d coins in this image" % (len(cnts)))
coins = image.copy()
cv.drawContours(coins, cnts, -1, (0,255,0),2)
cv.imshow("Coins",coins)
cv.waitKey(0)
cv.destroyAllWindows()