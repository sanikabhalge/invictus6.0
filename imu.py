import math
import serial
import time

def read_imu_data():
    try:
        # Set up the serial connection (adjust the COM port and baud rate as needed)
        ser = serial.Serial('COM4', 115200)  # Change 'COM4' to your Arduino port
        time.sleep(2)  # Wait for the connection to be established

        while True:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line.startswith("Ax:"):
                    data = line.split()
                    ax = int(data[0].split(':')[1])
                    ay = int(data[1].split(':')[1])
                    az = int(data[2].split(':')[1])
                    gx = int(data[3].split(':')[1])
                    gy = int(data[4].split(':')[1])
                    gz = int(data[5].split(':')[1])
                    a = math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
                    print(f"Ax: {ax}, Ay: {ay}, Az: {az}, Gx: {gx}, Gy: {gy}, Gz: {gz}")

                    # Return a and gz values
                    #return a, gz

            except Exception as e:
                print(f"Error reading data: {e}")
                break

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    try:
        a,gz=read_imu_data()
        #read_imu_data()


    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        # Clean up the serial connection if it was opened
        try:
            #ser.close()
            pass
        except NameError:
            pass
