import cv2 as cv


cam = cv.VideoCapture(0,cv.CAP_DSHOW)

if not cam.isOpened():
    raise IOError("Cannot open webcam")

while True:
    # ret is a boolean value returned by "read" function to check if frame  was captured successfully  or not.
    ret, frame = cam.read()
    #Resize the captured image
    # "fx","fy" for scale down 50% ,, "interpolation" for increase image up to help scale up
    frame =  cv.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)
    cv.imshow("Input",frame)
    #"waitkey()" for displaying image properly with a wait time for '1' millsieconds.
    c = cv.waitKey(1)
    #ASCII value of Esc os 27. Once  ESC Button is pressed, we break out from while loop.
    if c == 27:
        break

#"release" is used for  closing the webcam properly.
cam.release()

