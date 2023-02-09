import sys 
import viewer as gl 
import pyzed.sl as sl 
import math 
import cv2 
 
# Create a ZED camera 
zed = sl.Camera() 
init_params = sl.InitParameters() 
init_params.sdk_verbose = True # Enable verbose logging 
init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE # Set the depth mode to performance (fastest) 
init_params.coordinate_units = sl.UNIT.MILLIMETER  # Use millimeter units 
 
# Open the camera 
err = zed.open(init_params) 
if err != sl.ERROR_CODE.SUCCESS: 
    print("Error {}, exit program".format(err)) # Display the error 
    exit() 
 
print("Running Depth Sensing sample ... Press 'Esc' to quit") 
 
input_type = sl.InputType() 
 
init = sl.InitParameters(depth_mode=sl.DEPTH_MODE.ULTRA, 
                                coordinate_units=sl.UNIT.METER, 
                                coordinate_system=sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP, 
                                input_t=input_type 
                                ) 
zed = sl.Camera() 
status = zed.open(init) 
if status != sl.ERROR_CODE.SUCCESS: 
    print(repr(status)) 
    exit() 
 
res = sl.Resolution() 
res.width = 720 
res.height = 404 
 
camera_model = zed.get_camera_information().camera_model

# capture image and depth until i press q
image = sl.Mat() 
depth = sl.Mat() 
point_cloud = sl.Mat() 
runtime_parameters = sl.RuntimeParameters() 
 
while True: 
    # Grab an image 
    if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS: 
        # A new image is available if grab() returns sl.ERROR_CODE.SUCCESS 
        zed.retrieve_image(image, sl.VIEW.LEFT) # Get the left image 
        zed.retrieve_measure(depth, sl.MEASURE.DEPTH) # Retrieve depth matrix. Depth is aligned on the left RGB image 
        zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA) # Retrieve colored point cloud 
        i = i + 1 
        # Get and print distance value in mm at the center of the image 
    # We measure the distance camera - object using Euclidean distance 
    x = round(image.get_width() / 2) 
    y = round(image.get_height() / 2) 
    err, point_cloud_value = point_cloud.get_value(x, y) 
    distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] + 
                        point_cloud_value[1] * point_cloud_value[1] + 
                        point_cloud_value[2] * point_cloud_value[2]) 
    print("Distance to Camera at ({0}, {1}): {2} mm".format(x, y, distance), end="\r")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break