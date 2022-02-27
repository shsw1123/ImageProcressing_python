import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# imread Original file
image = cv.imread("Figures/MessiOriginal.jpg",0) # cv.imread("path",0 = gray scale values)
image2 = image.copy()
hSI, wSI = image.shape[:2]
print("Orginal Image: width=",wSI,",height=",hSI)
# imread template file
template = cv.imread("Figures/MessiTemplate.jpg",0)
hT, wT = template.shape[:2]
print("Template Image: width=",wT,",height=",hT)
# create a list of all 6 methods for matching comparison
methods = ["cv.TM_SQDIFF","cv.TM_SQDIFF_NORMED","CV.TM_CCOEFF",
           "cv.TM_CCOEFF_NORMED","cv.TM_CCORR","CV.TM_CCORR_NORMED"]
# for loop to test out all 6 methods for matching comparison
for meth in methods:
    image = image2.copy()
    # using each matching comparison method
    method = eval(meth) # meth is for loop
    print("method = ",methods[eval(meth)])
    # "matchTemplate" : apply template Matching
    Mresult = cv.matchTemplate(image,template,method)
    hM, wM = Mresult.shape[:2]
    print("Template Matching Image: width=",wM,"height=",hM)

    # "minMaxLoc" : find the global max/min values and its location

    min_val,max_val,min_loc,max_loc = cv.minMaxLoc(Mresult)
    print("minV = ",min_val,"MaxV = ",max_val)
