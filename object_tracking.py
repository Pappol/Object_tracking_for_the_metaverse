import cv2
import numpy as np
import argparse

def dummy(x):
    pass

def circularity(cnt):
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    return 4*np.pi*area/perimeter**2

def color_contorns(hsv, lower, upper, color):

    area = cv2.getTrackbarPos('area','image') / 100
    length_l = cv2.getTrackbarPos('length_l','image')
    length_u = cv2.getTrackbarPos('length_u','image')
    circ = cv2.getTrackbarPos('circularity','image') / 100
    #create a mask
    mask= cv2.inRange(hsv, lower, upper)
    #dilate the mask
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.dilate(mask, kernel, iterations = 1)
    #find the contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # keep only 20% of the contours
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:int(len(contours)*area) if int(len(contours)*area) > 0 else 1]
    # filter by boundary length
    contours = [cnt for cnt in contours if length_l < cv2.arcLength(cnt, True) < length_u]
    # filter by circularity
    contours = [cnt for cnt in contours if circ < circularity(cnt)]
    #find the center of the contours
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

#name the window
cv2.namedWindow('image')
#start the video capture
cap = cv2.VideoCapture(0)

cv2.createTrackbar('area','image',0,100, dummy)
cv2.createTrackbar('length_u','image',0,400, dummy)
cv2.createTrackbar('length_l','image',0,200, dummy)
cv2.createTrackbar('circularity','image',0,100, dummy)
cv2.setTrackbarPos('area','image',20)
cv2.setTrackbarPos('length_l','image',10)
cv2.setTrackbarPos('length_u','image',30)
cv2.setTrackbarPos('circularity','image',40)

#create a filter for different colors
#red
cv2.createTrackbar('RMinH','image',0,255, dummy)
cv2.createTrackbar('RMaxH','image',0,255, dummy)
cv2.createTrackbar('RMinS','image',0,255, dummy)
cv2.createTrackbar('RMaxS','image',0,255, dummy)
cv2.createTrackbar('RMinV','image',0,255, dummy)
cv2.createTrackbar('RMaxV','image',0,255, dummy)
cv2.setTrackbarPos('RMinH','image',0)
cv2.setTrackbarPos('RMaxH','image',20)
cv2.setTrackbarPos('RMinS','image',130)
cv2.setTrackbarPos('RMaxS','image',215)
cv2.setTrackbarPos('RMinV','image',135)
cv2.setTrackbarPos('RMaxV','image',255)
RMinH = RMaxH = RMinS = RMaxS = RMinV = RMaxV = 0
# lower_red = np.array([160,100,30])
# upper_red = np.array([180,255,255])
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
    # gaussian blur
    frame = cv2.GaussianBlur(frame, (5, 5), 2)
    #convert the frames to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #create a mask red
    RMinH = cv2.getTrackbarPos('RMinH','image')
    RMaxH = cv2.getTrackbarPos('RMaxH','image')
    RMinS = cv2.getTrackbarPos('RMinS','image')
    RMaxS = cv2.getTrackbarPos('RMaxS','image')
    RMinV = cv2.getTrackbarPos('RMinV','image')
    RMaxV = cv2.getTrackbarPos('RMaxV','image')
    # lower_red = np.array([0,130,135])
    # upper_red = np.array([20,215,255])
    lower_red = np.array([RMinH,RMinS,RMinV])
    upper_red = np.array([RMaxH,RMaxS,RMaxV])
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

    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    # mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
    # mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
    # mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)
    # mask_orange = cv2.morphologyEx(mask_orange, cv2.MORPH_CLOSE, kernel)
    # mask_yellow = cv2.morphologyEx(mask_yellow, cv2.MORPH_CLOSE, kernel)
    # mask_white = cv2.morphologyEx(mask_white, cv2.MORPH_CLOSE, kernel)

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
    cv2.imshow('image', frame)
    # cv2.waitKey(1)
    #cv2.imshow('mask', mask)
    #press q to exit
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.waitKey(0)
    # resume when space is pressed again
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.waitKey(1)
#release the capture
cap.release()
cv2.destroyAllWindows()
