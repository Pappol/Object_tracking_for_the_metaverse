import cv2
import numpy as np
import argparse

def color_contorns(hsv, lower, upper, color, frame):
    #create a mask
    mask = cv2.inRange(hsv, lower, upper)
    #find the contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #find the center of the contours
    for cnt in contours:
        #remove the small contours
        if cv2.contourArea(cnt) < 60:
            continue
        M = cv2.moments(cnt)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #draw a circle on the center of the contours
            cv2.circle(frame, (cx, cy), 10, color, -1)
            #draw the contours
            cv2.drawContours(frame, cnt, -1, color, 3)
    return frame

def object_tracking(white, red, green, blue, orange, yellow):

    #print all the color shapes
    print ("white")
    print (white[0]+10)
    print (white.shape)


    #start the video capture
    cap = cv2.VideoCapture(0)
    #create a filter for different colors
    #red
    lower_red = np.array(red[0])
    print (lower_red)
    upper_red = np.array([lower_red+10,255,255])
    print (upper_red)
    #green
    lower_green = np.array(green[0])
    upper_green = np.array([lower_green+10,255,255])
    #blue
    lower_blue = np.array(blue[0])
    upper_blue = np.array([lower_blue+10,255,255])
    #orange
    lower_orange = np.array(orange[0])
    upper_orange = np.array([lower_orange+10,255,255])
    #yellow
    lower_yellow = np.array(yellow[0])
    upper_yellow = np.array([lower_yellow+10,255,255])
    #white
    lower_white = np.array(white[0])
    upper_white = np.array([lower_white+10,255,255])

    #start the loop
    while cap.isOpened():
        #read the frames
        ret, frame = cap.read()
        #convert the frames to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #find the contours for red
        frame = color_contorns(hsv, lower_red, upper_red, (0,0,255), frame)
        #find the contours for green
        frame = color_contorns(hsv, lower_green, upper_green, (0,255,0), frame)
        #find the contours for blue
        frame = color_contorns(hsv, lower_blue, upper_blue, (255,0,0),  frame)
        #find the contours for orange
        frame = color_contorns(hsv, lower_orange, upper_orange, (0,165,255), frame)
        #find the contours for yellow
        frame = color_contorns(hsv, lower_yellow, upper_yellow, (0,255,255), frame)
        #find the contours for white
        frame = color_contorns(hsv, lower_white, upper_white, (255,255,255), frame)

        #show the frames
        cv2.imshow('frame', frame)
        #cv2.imshow('mask', mask)
        #press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #release the capture
    cap.release()
    cv2.destroyAllWindows()
