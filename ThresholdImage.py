import argparse
import numpy as np
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-image","--image",required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blurred = cv.GaussianBlur(image,(5,5),0)
cv.imshow("Gaussian blur",blurred)

# "threshold" to seg,emt image with illumination above 210 to 255 to select white background area
(T, thresh) = cv.threshold(blurred, 210, 255, cv.THRESH_BINARY)
cv.imshow("BINARY",thresh)
(T, thresh_INV) = cv.threshold(blurred, 210, 255, cv.THRESH_BINARY_INV)
cv.imshow("BINARY_INV",thresh_INV)

cv.imshow("Paper", cv.bitwise_and(image, image, mask=thresh_INV))
cv.waitKey(0)
cv.destroyAllWindows()
