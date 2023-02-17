import cv2 as cv
import os
import numpy as np

# termination criteria
CRITERIA = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
CALIB_DATA_PATH = "calib_data"

def check_calib_data():
    check_file = os.path.isfile(f"{CALIB_DATA_PATH}/MultiMatrix.npz")
    if check_file:
        print("Calibration data already exists")
        return True
    else:
        return False

def load_calib_data():
    calib_data = np.load(f"{CALIB_DATA_PATH}/MultiMatrix.npz")
    cam_mat = calib_data["camMatrix"]
    dist_coef = calib_data["distCoef"]
    r_vectors = calib_data["rVector"]
    t_vectors = calib_data["tVector"]
    return cam_mat, dist_coef, r_vectors, t_vectors

def create_dir():
    check_dir = os.path.isdir(CALIB_DATA_PATH)

    if not check_dir:
        os.makedirs(CALIB_DATA_PATH)
        print(f'Creating "{CALIB_DATA_PATH}" folder')

    else:
        print(f'"{CALIB_DATA_PATH}" folder already exists')

def calibrate_camera(chessBoardDim = (9, 6), squareSize = 250):
    
    print("Calibrating camera...")

    # create directory if not exists
    create_dir()

    # prepare object points
    obj_3D = np.zeros((chessBoardDim[0] * chessBoardDim[1], 3), np.float32)
    obj_3D[:, :2] = np.mgrid[0 : chessBoardDim[0], 0 : chessBoardDim[1]].T.reshape(-1, 2)
    obj_3D *= squareSize

    # Arrays to store object points and image points from all the images.
    obj_points_3D = []  # 3d point in real world space
    img_points_2D = []  # 2d points in image plane.

    cap = cv.VideoCapture(0)
    count = 0

    while count < 45:
        ret, image = cap.read()
        if not ret:
            break
        grayScale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        ret, corners = cv.findChessboardCorners(image, chessBoardDim, None)
        if ret == True:
            obj_points_3D.append(obj_3D)
            corners2 = cv.cornerSubPix(grayScale, corners, (3, 3), (-1, -1), CRITERIA)
            img_points_2D.append(corners2)
            image = cv.drawChessboardCorners(image, chessBoardDim, corners2, ret)

            count += 1

        cv.imshow("img", image)
        cv.waitKey(1)

    cap.release()
    cv.destroyAllWindows()
    
    # h, w = image.shape[:2]
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
        obj_points_3D, img_points_2D, grayScale.shape[::-1], None, None
    )
    print("Camera calibration completed")

    # save the data
    np.savez(f"{CALIB_DATA_PATH}/MultiMatrix",camMatrix=mtx,distCoef=dist,rVector=rvecs,tVector=tvecs)
    print("Data saved successfully")

if __name__ == "__main__":
    calibrate_camera()