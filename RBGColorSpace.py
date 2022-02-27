import argparse
import numpy as np
import cv2 as cv

Outdoor = cv.imread("Figures/Cube1.jpg")  # Figures is subFolder
Indoor = cv.imread("Figures/Cube8.jpg")

cv.imshow("Outdoor Cube Image",Outdoor)
cv.imshow("Indoor Cube Image",Indoor)
#  "Split" to unpack the image into  3 channels in (B,G,R) order.
# Each channel is represented as a ndarray with 2 dimension.
(Bo,Go,Ro) = cv.split(Outdoor)
BGRspeceo = np.hstack([Bo,Go,Ro])
cv.imshow("BGR space: Outdoor",BGRspeceo)

(Bi,Gi,Ri) = cv.split(Indoor)
BGRspecei =np.hstack([Bi,Gi,Ri])
cv.imshow("BGR space: Indoor",BGRspecei)

cv.waitKey(0)
cv.destroyAllWindows()