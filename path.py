# import numpy as np
# import imu
# import matplotlib.pyplot as plt
# import threading
# def plot_path(robot_path):
#     plt.ion()
#     fig, ax = plt.subplots()
#     line, = ax.plot([], [], 'b-')
#     ax.set_xlim(-10000, 10000)
#     ax.set_ylim(-10000, 10000)
#
#     while True:
#         if len(robot_path.path) > 0:
#             x, y = zip(*robot_path.path)
#             line.set_xdata(x)
#             line.set_ydata(y)
#             ax.relim()
#             ax.autoscale_view()
#             plt.draw()
#             plt.pause(0.01)
#
# class RobotPath:
#     def __init__(self):
#         self.x = 0.0
#         self.y = 0.0
#
#     def update_position(self, imu_acceleration, dt):
#         # Integrate acceleration to estimate velocity
#         velocity = imu_acceleration * dt
#
#         # Integrate velocity to estimate position
#         self.x += velocity * np.cos(self.yaw) * dt
#         self.y += velocity * np.sin(self.yaw) * dt
#
#     def set_yaw(self, imu_yaw):
#         self.yaw = imu_yaw
#
# # Example usage:
# if __name__ == "__main__":
#     robot_path = RobotPath()
#     dt = 0.1 # Time step (adjust as needed)
#     print('p')
#
#     while True:
#         imu_acceleration,imu_yaw=imu.read_imu_data()  # Replace with actual IMU data
#     # Replace with actual IMU yaw angle
#
#         robot_path.set_yaw(imu_yaw)
#         robot_path.update_position(imu_acceleration, dt)
#         print(f"Estimated position: ({robot_path.x:.2f}, {robot_path.y:.2f})")

import numpy as np
import threading
import matplotlib.pyplot as plt
import imu  # Assuming 'imu' is a module that reads IMU data
class RobotPath:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.path = []

    def update_position(self, imu_acceleration, dt):
        # Integrate acceleration to estimate velocity
        velocity = imu_acceleration * dt

        # Integrate velocity to estimate position
        self.x += velocity * np.cos(self.yaw) * dt
        self.y += velocity * np.sin(self.yaw) * dt

        # Append current position to path
        self.path.append((self.x, self.y))

    def set_yaw(self, imu_yaw):
        self.yaw = imu_yaw
def plot_path(robot_path):

        global is_plot
        plt.ion()
        fig, ax = plt.subplots()
        is_plot = True

        while is_plot:
            ax.cla()
            ax.set_xlim(-0.25, 0.25)
            ax.set_ylim(-0.25, 0.25)


            if len(robot_path.path) > 0:
                x, y = zip(*robot_path.path)
                ax.scatter(x, y, c='r', s=8)

            plt.pause(0.001)

        plt.close(fig)


if __name__ == "__main__":
    robot_path = RobotPath()
    dt = 0.001  # Time step (adjust as needed)

    # Start the plotting thread
    plot_thread = threading.Thread(target=plot_path, args=(robot_path,))
    plot_thread.daemon = True
    plot_thread.start()

    while True:
        imu_acceleration, imu_yaw = imu.read_imu_data()  # Replace with actual IMU data
        robot_path.set_yaw(imu_yaw)
        robot_path.update_position(imu_acceleration, dt)
        print(f"Estimated position: ({robot_path.x:.2f}, {robot_path.y:.2f})")
