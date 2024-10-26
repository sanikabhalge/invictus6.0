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

dac.py: in this module used for throttle voltage change for this install sudo apt-get update
sudo apt-get install -y python3-pip
pip3 install adafruit-blinka
pip3 install Adafruit-Blinka
pip3 install adafruit-circuitpython-mcp4725
then make amcp_4725.py file 
connection dac use i2c pins jetson pin no 4-vcc(5V) pin 6:GND pin 3:sda pin 5:scl  // changed the ic to iso1540(isolated gnd) as this dac was making the hv and autonomous gnd same (not done yet)

servo.py:use to control steering connected using ftdi to uart pins to jetson . //not going to use it it was for robu motor.

mosfet.py:used to control actuator connecte to pin 29 of jetson .the second code is for 2mosfet with common gnd proto on jetson xavier nx(s).

uart.py:it was used to communicate with esp32 of indicator through uart things .we tried at first using pin 8-rx2 ,pin10-tx2,gnd-gnd but it was not working .to make it work we first change the permission and added dialout in group now will try for loopback .
was not able to work with GPIO pins so tried ftdi for uart  proto on jetson xavier nx(s).
