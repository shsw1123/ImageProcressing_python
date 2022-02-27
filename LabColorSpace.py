import cv2 as cv
import numpy as np
import argparse
# Imread
Outdoor = cv.imread("Figures/Cube1.jpg")  # Figures is subFolder
Indoor = cv.imread("Figures/Cube8.jpg")

# "cvtcolor" for convert image from one color space to another color space
Outdoor = cv.cvtColor(Outdoor, cv.COLOR_BGR2LAB)
Indoor = cv.cvtColor(Indoor, cv.COLOR_BGR2LAB)

cv.imshow("Outdoor",Outdoor)
cv.imshow("Indoor",Indoor)

# "L" for Lightness, "a" for color component ranging from green to magenta,
# "b" for color component ranging from Blue to yellow
(Lo,ao,bo) = cv.split(Outdoor)
(Li,ai,bi) = cv.split(Indoor)
Labspaceo = np.hstack([Lo,ao,bo])
Labspacei = np.hstack([Li,ai,bi])
cv.imshow("Outdoor",Labspaceo)
cv.imshow("Indoor",Labspacei)

cv.waitKey(0)
cv.destroyAllWindows()
