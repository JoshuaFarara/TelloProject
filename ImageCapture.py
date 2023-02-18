from djitellopy import tello
import cv2 #

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon() # image acquisition with frames 1 by 1.

while True:  # continuous number of frames so use while loop
    img = me.get_frame_read().frame  # gives individual image from tello
    img = cv2.resize(img, (360,240)) #resizing to smaller frame for image process speed purposes, size of the resizing ( ,)
    cv2.imshow("Image", img)  # creates window to display the result, which is the img
    cv2.waitKey(1) #without this frame will shut down before we can see output, must have delay, given 1 millisecond
