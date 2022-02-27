import argparse as arg
import cv2 as cv
#  "ArgumentParser" is creating an object to  parse the command  line into  python data.
ap = arg.ArgumentParser(description="Load Image.")
# "add_argument" to take  the strings on the command line and turn them into objects
ap.add_argument("-i","--image",required=True,help="path to an input-image file")

args = vars(ap.parse_args())

image = cv.imread(args["image"])

print("width: %d pixels" % (image.shape[1]))
print("height: %d  pixels" % (image.shape[0]))
print("Channels: %d" % (image.shape[2]))

cv.imshow("Inputed  Image",image)
# waitKey(0) display  image for infinite time until Esc key is  pressed.
cv.waitKey(0)
cv.destroyWindow("Inputed Image")
