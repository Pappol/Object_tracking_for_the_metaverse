import cv2
import numpy as np
import argparse

def color_contorns(hsv, lower, upper, color):
    #create a mask
    mask= cv2.inRange(hsv, lower, upper)
    #find the contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #sort the contours by area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:int (0.1*len(contours))]
    for cnt in contours:
        #filter for small areas
        M = cv2.moments(cnt)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #draw a circle on the center of the contours
            cv2.circle(frame, (cx, cy), 10, color, -1)
        #draw the contours
        cv2.drawContours(frame, contours, -1, color, 3)
    return frame

#start the video capture
cap = cv2.VideoCapture(0)
#create a filter for different colors
#red
lower_red = np.array([0,100,150])
upper_red = np.array([7,255,255])
#green
lower_green = np.array([40,100,30])
upper_green = np.array([80,255,255])
#blue
lower_blue = np.array([100,100,30])
upper_blue = np.array([140,255,255])
#orange
lower_orange = np.array([7,100,150])
upper_orange = np.array([20,255,255])
#yellow
lower_yellow = np.array([20,100,30])
upper_yellow = np.array([40,255,255])
#white
lower_white = np.array([0,0,0])
upper_white = np.array([50,50,255])

#start the loop
while cap.isOpened():
    #read the frames
    ret, frame = cap.read()
    #convert the frames to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #create a mask red
    mask_red= cv2.inRange(hsv, lower_red, upper_red)
    #create a mask green
    mask_green= cv2.inRange(hsv, lower_green, upper_green)
    #create a mask blue
    mask_blue= cv2.inRange(hsv, lower_blue, upper_blue)
    #create a mask orange
    mask_orange= cv2.inRange(hsv, lower_orange, upper_orange)
    #create a mask yellow
    mask_yellow= cv2.inRange(hsv, lower_yellow, upper_yellow)
    #create a mask white
    mask_white= cv2.inRange(hsv, lower_white, upper_white)

    #find the contours for red
    frame = color_contorns(hsv, lower_red, upper_red, (0,0,255))
    #find the contours for green
    frame = color_contorns(hsv, lower_green, upper_green, (0,255,0))
    #find the contours for blue
    frame = color_contorns(hsv, lower_blue, upper_blue, (255,0,0))
    #find the contours for orange
    frame = color_contorns(hsv, lower_orange, upper_orange, (0,165,255))
    #find the contours for yellow
    frame = color_contorns(hsv, lower_yellow, upper_yellow, (0,255,255))
    #find the contours for white
    frame = color_contorns(hsv, lower_white, upper_white, (255,255,255))

    #show the frames
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    #press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release the capture
cap.release()
cv2.destroyAllWindows()
