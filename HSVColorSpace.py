# HSV Color space
# V channel represent Intensity (ความเข้ม)
# H = Hue ( Dominant Wavelength )
# S = Saturation ( Purity / Shades of the color. )
# V = Value of Intensity
import cv2 as cv
import numpy as np
Outdoor = cv.imread("Figures/Cube1.jpg")
Indoor = cv.imread("Figures/Cube8.jpg")

HSVo = cv.cvtColor(Outdoor,cv.COLOR_BGR2HSV)
HSVi = cv.cvtColor(Indoor,cv.COLOR_BGR2HSV)
cv.imshow("Outdoor",Outdoor)
cv.imshow("Indoor",Indoor)
(Ho,So,Vo) = cv.split(HSVo)
(Hi,Si,Vi) = cv.split(HSVi)
HSVspaceo = np.hstack([Ho,So,Vo])
HSVspacei = np.hstack([Hi,Si,Vi])

cv.imshow("HSVo space",HSVspaceo)
cv.imshow("HSVi space",HSVspacei)
cv.waitKey(0)
cv.destroyAllWindows()

