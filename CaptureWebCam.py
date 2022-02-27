import cv2 as cv


cam = cv.VideoCapture(0,cv.CAP_DSHOW)

if not cam.isOpened():
    raise IOError("Cannot open webcam")

# ret is a boolean value returned by "read" function to check if frame  was captured successfully  or not.
ret, frame = cam.read()
if ret:
    cv.imshow("SnapshotTest",frame)
    cv.waitKey(1)
    cv.destroyWindow('SnapshotTest')
    cv.imwrite("SnapshotImage2.jpg",frame)

cam.release()