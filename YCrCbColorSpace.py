# YCrCb space, luminance and chrominance components are separated into diffent channels.
# Mostly used in compression for TV Transmission.
# Y = Luminance or Luma component  obthained from RGB after gamma correction.
# Cr = R-Y
# Cb = B-Y
import cv2 as cv
import numpy as np
Outdoor = cv.imread("Figures/Cube1.jpg")
Indoor = cv.imread("Figures/Cube8.jpg")
OutdoorYCrCb = cv.cvtColor(Outdoor,cv.COLOR_BGR2YCrCb)
IndoorYCrCb = cv.cvtColor(Indoor,cv.COLOR_BGR2YCrCb)
cv.imshow("ConvertColor_OUT",Outdoor)
cv.imshow("ConvertColor_IN",Indoor)

(Yo,Cro,Cbo) = cv.split(OutdoorYCrCb)
(Yi,Cri,Cbi)  = cv.split(IndoorYCrCb)
YCrCbspaceo = np.hstack([Yo,Cro,Cbo])
YCrCbspacei = np.hstack([Yi,Cri,Cbi])

cv.imshow("YCrCbspaceo",YCrCbspaceo)
cv.imshow("YCrCbspacei",YCrCbspacei)

cv.waitKey(0)
cv.destroyAllWindows()