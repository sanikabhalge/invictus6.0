import cv2
import time
import torch
import numpy as np
from ultralytics import YOLO
import color_seg
import csv
import PyLidar3
import matplotlib.pyplot as plt
import math
import threading


def lidar_process():
    global is_plot

    def draw():
        global is_plot
        while is_plot:
            plt.figure(1)
            plt.cla()
            plt.ylim(-9000, 9000)
            plt.xlim(-9000, 9000)
            plt.scatter(x, y, c='r', s=8)
            plt.pause(0.001)
        plt.close("all")

    is_plot = True
    x = [0] * 360  # Initialize x with 360 zeros
    y = [0] * 360  # Initialize y with 360 zeros

    port = input("Enter port name which lidar is connected:")  # windows
    Obj = PyLidar3.YdLidarG4(port)  # PyLidar3.your_version_of_lidar(port,chunk_size)
    threading.Thread(target=draw).start()
    threading.Thread(target=object_detection).start()
    try:
        if Obj.Connect():
            print(Obj.GetDeviceInfo())
            gen = Obj.StartScanning()
            while True:  # Run indefinitely until stopped externally or by keyboard interrupt
                data = next(gen)
                for angle in range(360):
                    if data[angle] > 1000:
                        x[angle] = data[angle] * math.cos(math.radians(angle))
                        y[angle] = data[angle] * math.sin(math.radians(angle))


    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Stopping scanning.")
        is_plot = False
        Obj.StopScanning()
        Obj.Disconnect()
    except Exception as e:
        print("An error occurred:", e)


# Function for object detection
def object_detection():
    cap = cv2.VideoCapture(0)
    model = YOLO(r"C:\pd_anomaly_detection\PD___Anomaly_Detection\runs\detect\train3\weights\best.pt")
    model.conf = 0.4  # Adjust confidence threshold for detection
    model.to('cuda:0')
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    coco_classes = ["background", "blue_cone", "large_orange_cone", "orange_cone", "unknown_cone", "yellow_cone"]

    while True:
        ret, img = cap.read()
        if not ret:
            break

        results = model.predict(img, stream=True)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1
                class_index = int(box.cls[0])
                confidence = box.conf[0]
                cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 0))

        resizedi = cv2.resize(img, (680, 420))
        cv2.imshow("original", resizedi)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Start threading for lidar
threading.Thread(target=lidar_process).start()
