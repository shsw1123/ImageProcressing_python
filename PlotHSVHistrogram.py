import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread("Figures/GreenColor.jpg")

imageHSV = cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow("Original HSV",imageHSV)
(Hue, Sat, Val) = cv.split(imageHSV)
cv.imshow("Hue space",Hue)
histHue = cv.calcHist(Hue,[0],None, [255],[0,255])
histSat = cv.calcHist(Sat,[0],None, [255],[0,255])
histVal = cv.calcHist(Val,[0],None, [255],[0,255])
plt.figure()
plt.title("Hue,Sat,Val")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(histHue,'b')
plt.plot(histSat,'r')
plt.plot(histVal,'g')
plt.legend(('Hue','Sat','Val'))
plt.xlim([0,255])
plt.show()

cv2.waitKey(0)
cv.destroyAllWindows()