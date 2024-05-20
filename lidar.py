# import PyLidar3
# import time # Time module
# #Serial port to which lidar connected, Get it from device manager windows
# #In linux type in terminal -- ls /dev/tty*
# port = input("Enter port name which lidar is connected:") #windows
# #port = "/dev/ttyUSB0" #linux
# Obj = PyLidar3.YdLidarG4(port) #PyLidar3.your_version_of_lidar(port,chunk_size)
# if(Obj.Connect()):
#     print(Obj.GetDeviceInfo())
#     gen = Obj.StartScanning()
#     t = time.time() # start time
#     while (time.time() - t) < 30: #scan for 30 seconds
#         print(next(gen))
#         time.sleep(0.5)
#     Obj.StopScanning()
#     Obj.Disconnect()
# else:
# #     print("Error connecting to device")
# import PyLidar3
# import matplotlib.pyplot as plt
# import math
# import threading
#
# def draw():
#     global is_plot
#     while is_plot:
#         plt.figure(1)
#         plt.cla()
#         plt.ylim(-9000, 9000)
#         plt.xlim(-9000, 9000)
#         plt.scatter(x, y, c='r', s=8)
#         plt.pause(0.001)
#     plt.close("all")
#
# is_plot = True
# x = [0] * 360  # Initialize x with 360 zeros
# y = [0] * 360  # Initialize y with 360 zeros
#
# port = input("Enter port name which lidar is connected:")  # windows
# Obj = PyLidar3.YdLidarG4(port)  # PyLidar3.your_version_of_lidar(port,chunk_size)
# threading.Thread(target=draw).start()
# Obj.Reset()
# if Obj.Connect():
#     print(Obj.GetDeviceInfo())
#     gen = Obj.StartScanning()
#     while True:  # Run indefinitely until stopped externally
#         data = next(gen)
#         for angle in range(360):
#             if data[angle] > 1000:
#                 x[angle] = data[angle] * math.cos(math.radians(angle))
#                 y[angle] = data[angle] * math.sin(math.radians(angle))
# else:
#     print("Error connecting to device")
import PyLidar3
import matplotlib.pyplot as plt
import math
import threading

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



