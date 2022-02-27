import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Upload Picture
bird = cv.imread("Figures/BirdPic.jpg")
cv.imshow("Original",bird)
# Convert RGB to gray scale
bird_g = cv.cvtColor(bird,cv.COLOR_BGR2GRAY)
# Blurred
blurred = cv.GaussianBlur(bird_g,(5,5),0)
#cv.imshow("blurred Image",blurred)
# Threshold
(T,thres) = cv.threshold(blurred,170,250,cv.THRESH_BINARY)
cv.imshow("threshold Image", thres)
# Detect-Edge
edge = cv.Canny(thres,50,150)
cv.imshow("Detect-Edge-Canny ",edge)
# Contours
cnts, hierarchy = cv.findContours(edge,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

print("There are %d birds in this image" % (len(cnts)))
bird_c = bird.copy()
cv.drawContours(bird_c,cnts,-1,(0,255,0),2)
cv.imshow("Contours",bird_c)


#plt.subplot(221), plt.imshow(bird,"gray"), plt.title("Original")
#plt.subplot(222), plt.imshow(thres,"gray"), plt.title("Threshold")
#plt.subplot(223), plt.imshow(edge,"gray"), plt.title("Detect-Edge")
#plt.subplot(224), plt.imshow(bird_c,"gray"),plt.title("Contours")
#plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
