import cv2
import numpy as np

def compute_rotation(red, green, blue, orange, yellow, white, frame):
    #compute the total area
    total_area = red + green + blue + orange + yellow + white
    if total_area < 10:
        return frame
    #compute the percentage of each color
    red_perc = red/total_area
    green_perc = green/total_area
    blue_perc = blue/total_area
    orange_perc = orange/total_area
    yellow_perc = yellow/total_area
    white_perc = white/total_area
    # green front, orange right, red left, blue back, yellow top, white bottom
    # print text on frame based on the percentage of each color
    if red_perc > 0.1:
        cv2.putText(frame, 'LEFT', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    if green_perc > 0.1:
        cv2.putText(frame, 'FRONT', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if blue_perc > 0.1:
        cv2.putText(frame, 'BACK', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    if orange_perc > 0.1:
        cv2.putText(frame, 'RIGHT', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
    if yellow_perc > 0.1:
        cv2.putText(frame, 'TOP', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    if white_perc > 0.1:
        cv2.putText(frame, 'BOTTOM', (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


def dummy(x):
    pass

def circularity(cnt):
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    return 4*np.pi*area/perimeter**2

def color_contorns(hsv, lower, upper, color):

    area = cv2.getTrackbarPos('area','image') / 100
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
    contours = [cnt for cnt in contours if cv2.arcLength(cnt, True) > 100]
    # filter by circularity
    contours = [cnt for cnt in contours if circ < circularity(cnt)]
    #find the center of the contours
    for cnt in contours:
        cv2.drawContours(frame, contours, -1, color, 3)
        area += cv2.contourArea(cnt)

    return frame, area

#name the window
cv2.namedWindow('image')
#start the video capture
cap = cv2.VideoCapture(0)

cv2.createTrackbar('area','image',0,100, dummy)
cv2.createTrackbar('circularity','image',0,100, dummy)
cv2.setTrackbarPos('area','image',50)
cv2.setTrackbarPos('circularity','image',45)

#create a filter for different colors
#red
lower_red = np.array([0,130,135])
upper_red = np.array([20,215,255])
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
    frame, red_area = color_contorns(hsv, lower_red, upper_red, (0,0,255))
    #find the contours for green
    frame, green_area = color_contorns(hsv, lower_green, upper_green, (0,255,0))
    #find the contours for blue
    frame, blue_area = color_contorns(hsv, lower_blue, upper_blue, (255,0,0))
    #find the contours for orange
    frame, orange_area = color_contorns(hsv, lower_orange, upper_orange, (0,165,255))
    #find the contours for yellow
    frame, yellow_area = color_contorns(hsv, lower_yellow, upper_yellow, (0,255,255))
    #find the contours for white
    frame, white_area = color_contorns(hsv, lower_white, upper_white, (255,255,255))

    compute_rotation(red_area, green_area, blue_area, orange_area, yellow_area, white_area, frame)

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
