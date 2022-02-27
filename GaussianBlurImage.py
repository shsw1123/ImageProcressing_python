import argparse
import numpy as np
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)

blurred = np.hstack([
    cv.GaussianBlur(image,(3,3),0),
    cv.GaussianBlur(image,(5,5),0),
    cv.GaussianBlur(image, (7,7),0)
])
cv.imshow("GaussianBlur", blurred)
cv.waitKey(0)
cv.destroyAllWindows()