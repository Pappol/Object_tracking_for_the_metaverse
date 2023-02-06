import cv2
import numpy as np
import argparse
import random
import glob
import object_tracking




# a function that on mouse click will return the color of the pixel
def onclick(event, x, y, flags, param):
    global img 
    global counter
    global colori
    #get the color of the pixel
    if event == cv2.EVENT_LBUTTONDOWN:
        color = img[y, x]
        #convert to hsv
        hsv = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)
        #print the hsv value
        colori[counter] = hsv
        counter = counter + 1
        print(hsv)
        #print the next color to click
        if counter == 1:
            print ("select the color red")
        elif counter == 2:
            print ("select the color green")
        elif counter == 3:
            print ("select the color blue")
        elif counter == 4:
            print ("select the color orange")
        elif counter == 5:
            print ("select the color yellow")


def main(args):
    #import image
    global img 
    global counter
    global colori
    colori = np.zeros((6,1,3), np.uint8)

    counter = 0
    print ("select the color white")
    img = cv2.imread(args.image)
    #show the image and set on click function
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', onclick)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("colori")
    print (colori)
    print (colori.shape)
    print (colori[0].shape)
    object_tracking.object_tracking(colori[0][0], colori[1][0], colori[2][0], colori[3][0], colori[4][0], colori[5][0])

#ifdef main
if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the image")
    args = ap.parse_args()

    main(args)