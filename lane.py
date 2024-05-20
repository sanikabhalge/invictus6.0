# import cv2
# import time
# import torch
# import numpy as np
# from ultralytics import YOLO
# import color_seg
# import csv
# # Open the video file
# #vid_path=r"C:\sanikabhalge\test photos field\IMG_4720.mp4" #red cones
# #vid_path=r"C:\sanikabhalge\test photos field\IMG_4724.jpg"
# vid_path=r"C:\sanikabhalge\test photos field\IMG_4727.mp4"
# cap = cv2.VideoCapture(vid_path)
#
# #Set the width and height for video frames
# des_width = 1280
# des_height = 720
#
# # Set the resolution of the video capture
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, des_width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, des_height)
#
# # Load YOLO model
# model = YOLO(r"C:\pd_anomaly_detection\PD___Anomaly_Detection\runs\detect\train3\weights\best.pt")
# model.conf = 0.4  # Adjust confidence threshold for detection
# print(torch.cuda.is_available())
# model.to('cuda:0')
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# print(f'Using device: {device}')
#
# coco_classes = [
#     "background",
# "blue_cone",
# "large_orange_cone",
# "orange_cone",
# "unknown_cone",
# "yellow_cone"
# ]
#
#
# xb=0
# yb=0
# xy=0
# yy=0
# mx=0
# my=0
# pr_time=time.time()
# count=0
#
# while True:
#     # Read a frame from the video
#     ret, img = cap.read()
#
#     # if the frame is read
#     if not ret:
#         break
#
#     # Flip the image horizontally
#
#
#     # Perform object detection using YOLO
#     results = model.predict(img, stream=True)
#
#     # Process detection results
#
#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#
#             w, h = x2 - x1, y2 - y1
#             class_index = int(box.cls[0])
#             # Access class labels directly
#             confidence = box.conf[0]
#             cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,0,0))
#
#             #cv2.putText(img, f"{str(int(class_index))}class index", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (225, 0, 0), 3)
#             if(class_index==1 ):
#                 cv2.line(img,(xb,yb),(x1,y1),(0,0,0),3)
#
#                 xb,yb=x1,y1
#             if (class_index == 5):
#                 cv2.line(img, (xy, yy), (x1, y1), (0, 0, 0), 3)
#
#                 xy, yy = x1, y1
#             # if(class_index==2 or class_index==3):
#             #     cv2.line(img, (xy, yy), (x1, y1), (0,0,0), 3)
#             #     line=line+1
#             #     xy, yy = x1, y1
#     blackonly=color_seg.black_only(img)
#     roadframe=color_seg.road_frame(img)
#     plotroi=color_seg.plot_roi(img)
#     #cv2.imwrite('frame%d.jpg' %count,img)
#     count+=1
#     curr_time = time.time()
#     fps = 1 / (curr_time - pr_time)
#     pr_time = curr_time
#
#     # Display FPS on the image
#     cv2.putText(img, f"{str(int(fps))}fps", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (225, 0, 0), 3)
#     # Show the final image
#     resizedb = cv2.resize(blackonly, (680, 420))
#     resizedr= cv2.resize(roadframe, (680, 420))
#     #resizedm= cv2.resize(image, (680, 420))
#     resizedpr = cv2.resize(roadframe, (680, 420))
#     resizedi= cv2.resize(img, (680, 420))
#     cv2.imshow("roadframe", resizedr)
#     cv2.imshow("blackonly", resizedb)
#     cv2.imshow("plotroi", resizedpr)
#     #cv2.imshow("main", resizedm)
#     cv2.imshow("original",resizedi)
#     # Break the loop if the 'Esc' key is pressed
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
#
# # Release the video capture
# cap.release()
# cv2.destroyAllWindows()
# #file1.close()
# # with open('file.csv', 'w', newline='') as file:
# #     writer = csv.writer(file, delimiter=';', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# #     writer.writerow(data)
import cv2
import time
import torch
from ultralytics import YOLO
import color_seg
import numpy as np
# Path to the video file
vid_path = r"C:\invictus6\images\cam_video1.mp4"
cap = cv2.VideoCapture(0)

# Set the resolution of the video capture
des_width = 1280
des_height = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, des_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, des_height)

# Load YOLO model
model = YOLO(r"C:\pd_anomaly_detection\PD___Anomaly_Detection\runs\detect\train3\weights\best.pt")
model.conf = 0.4  # Adjust confidence threshold for detection
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)
print(f'Using device: {device}')

xb = yb = xy = yy = 0
pr_time = time.time()
count = 0

while True:
    ret, img = cap.read()
    if not ret:
        break
    if count==0:
        r = color_seg.select_roi(img)
        count = 1
    img= img[int(r[1]):int(r[1] + r[3]),
                    int(r[0]):int(r[0] + r[2])]
    results = model.predict(img, stream=True)
    for result in results:
         for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_index = int(box.cls[0])
            if class_index == 1 :
                cv2.line(img, (xb, yb), (x2, y2), (0, 0, 0), 3)
                xb, yb = x2, y2
            elif class_index == 5:
                cv2.line(img, (xy, yy), (x2, y2), (0, 0, 0), 3)
                xy, yy = x2, y2
            midpointx=(xb-xy)//2
            midpointy=np.absolute(((yb-yy)//2))
            center=(midpointx,midpointy)
            # print(center)
            cv2.circle(img,center,5,(0,0,0),7)
            # if class_index==5:
            #     xy1, yy1, xy2, yy2 = map(int, box.xyxy[0])
            #     print(xy2, yy2)
            #     cv2.line(img, (xb, yb), (xy1+640, yy1), (0, 0, 0), 3)
            #     xb, yb = xy1+640, yy1
            #     cv2.rectangle(img,(xy1, yy1),( xy2, yy2 ),(0,0,0),3)
    cv2.circle(img,(640 ,720),3,(0,0,0),7)
    blackonly = color_seg.black_only(img)
   # roadframe = color_seg.road_frame(img)
   # kuchkar=color_seg.kuchkar(img)
    plotroi = color_seg.getROI(img)

    count += 1
    curr_time = time.time()
    fps = 1 / (curr_time - pr_time)
    pr_time = curr_time

    cv2.putText(img, f"{str(int(fps))}fps", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (225, 0, 0), 3)

    #resizedb = cv2.resize(blackonly, (680, 420))
    #resizedr = cv2.resize(roadframe, (680, 420))
    #resizedi = cv2.resize(img, (680, 420))
    #resizedk = cv2.resize(kuchkar, (680, 420))
    #cv2.imshow("roadframe", resizedr)
    cv2.imshow("blackonly", blackonly)
    cv2.imshow("original", img)
    #cv2.imshow("kuchkar", resizedk)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



