import cv2 as cv
from cv2 import aruco
import numpy as np
from camera_calibaration import check_calib_data, calibrate_camera, load_calib_data

if not check_calib_data():
    calibrate_camera()

cam_mat, dist_coef, r_vectors, t_vectors = load_calib_data()

MARKER_SIZE = 3  # centimeters

# relative center of the cube given a face of the cube
# MARKER_SIZE is not divided by 2 because the marker is half the size of the cube
CUBE_CENTER = np.array([0, 0, -MARKER_SIZE]) 

# relative rotation of the cube given a face of the cube knowing marker 1 is the front face
RELATIVE_ROTATIONS = {
    0: np.array([-np.pi/2, 0, 0]).reshape((1, 3)),
    1: np.array([0, 0, 0]).reshape((1, 3)),
    2: np.array([0, -np.pi/2, 0]).reshape((1, 3)),
    3: np.array([0, np.pi, 0]).reshape((1, 3)),
    4: np.array([0, np.pi/2, 0]).reshape((1, 3)),
    5: np.array([np.pi/2, 0, 0]).reshape((1, 3)),
}

def sum_rvec(rvec1, rvec2):
    """ Sum two rvecs. """
    rvec1, rvec2 = rvec1.reshape((3, 1)), rvec2.reshape((3, 1))
    R1, _ = cv.Rodrigues(rvec1)
    R2, _ = cv.Rodrigues(rvec2)
    R = np.dot(R1, R2)
    rvec, _ = cv.Rodrigues(R)
    return rvec

def update_rotation(rvec, marker_id):
    """ Update the rotation vector. """
    return sum_rvec(rvec, RELATIVE_ROTATIONS[marker_id]).reshape((1, 3)) if marker_id != 1 else rvec

def centroid(rvec, tvec):
    """ Get the center of the cube in the camera coordinate system. """
    # Convert the rotation vector to a rotation matrix
    rmat, _ = cv.Rodrigues(rvec)

    # Transform the 4 vertices of the marker to the camera coordinate system
    center_camera = np.dot(rmat, CUBE_CENTER.T).T + tvec

    return center_camera


# initialize aruco dictionary and parameters
marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
param_markers = aruco.DetectorParameters_create()

cap = cv.VideoCapture(0)

# get cap width and height
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# create video writer for mp4
# writer = cv.VideoWriter(
#     'output.mp4',
#     cv.VideoWriter_fourcc(*"mp4v"),
#     30,
#     (width, height),
# )

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )

    # filter out markers that are not in the dictionary (keep only 0-5)
    if marker_IDs is not None:
        marker_IDs = marker_IDs.flatten()
        marker_corners = [marker_corners[i] for i in range(len(marker_IDs)) if marker_IDs[i] in range(6)]
        marker_IDs = [marker_IDs[i] for i in range(len(marker_IDs)) if marker_IDs[i] in range(6)]

    # if valid markers are found
    if marker_corners:
        # get rotation and translation vectors
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(
            marker_corners, MARKER_SIZE, cam_mat, dist_coef
        )

        # get id of max marker area and its rvec and tvec
        id = np.argmax([cv.contourArea(c) for c in marker_corners])
        rVec, tVec = rVec[id], tVec[id]

        # compute centroid and rotation of the cube
        tVec = centroid(rVec, tVec)
        rVec = update_rotation(rVec, marker_IDs[id])

        # draw axis
        cv.drawFrameAxes(frame, cam_mat, dist_coef, rVec, tVec, 3)

    # writer.write(frame)
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
# writer.release()
cv.destroyAllWindows()
