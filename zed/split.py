import cv2
import numpy as np
import argparse

def main(args):

    #import video
    cap = cv2.VideoCapture(args.input)

    #get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    #define video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(args.output, fourcc, fps, (width, height))

    #loop through video
    for i in range(frames):
        ret, frame = cap.read()
        if ret:
            #split frame in half width
            frame = frame[:, :int(width/2), :]
            #write frame to video
            out.write(frame)
    
    #release video
    cap.release()

if __name__ == "__main__":
    #define arguments
    parser = argparse.ArgumentParser(description='split the video in half width')
    parser.add_argument('input', type=str, help='Path to original video file')
    parser.add_argument('output', type=str, help='Path to AVI file')

    #parse arguments
    args = parser.parse_args()

    main(args)