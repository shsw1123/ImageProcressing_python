import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)

corner = image[190:320, 200:370]
cv2.imshow("T-Letter Image", corner)

# Assign above sliced-matrix image with red color
image[190:320,200:370] = (0,255,0)
cv2.imshow("Modify Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()