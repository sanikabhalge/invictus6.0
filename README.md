# invictus6.0
autonomous round esvc 2024

best100000imagesconf0.54.pt:it has dataset that contain 100000 images from solarium cones,amz racing ,and other racing car data.it has been trained for 121 epochs and achieved 0.54 MAP.it has 5 classes["background", "blue_cone", "large_orange_cone", "orange_cone", "unknown_cone", "yellow_cone" ]

pytorch_req.txt:for cuda setup
req.txt:for library requirements

train.py:contain a script to train a model from a pretrained model on custom dataset.
videocapture.py:used only to record the video in mp4 format
lidar.py:commented script is for both linux and windows .example is for windows
imu.py:it is to read imu data and get ax,ay,az,gx,gy,gz values .not working properly.need furthur development.  
path.py:used to learn the imu coordinate when it is moving and plot it to make a path.the imu.py is called in it.need furthur development
main.py:both lidar and camera are run simultaneously.

color_seg.py:
blackonly(img) :gives a masked image with black in the img is being shown as white and everything is masked.
road_frame(img):to draw lane lines not used.
kuchkar(img):it return black lines only
select_roi(img):to select a region of interest

lane.py:we select a roi for video stream.camera capture and put bounding boxes .draws lines.
