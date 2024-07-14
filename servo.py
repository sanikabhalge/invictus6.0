import serial
import time

# Configure serial port
ser = serial.Serial(
    port='/dev/ttyUSB0',  # Replace with your UART port on Jetson
    baudrate=9600,
    timeout=1  # 1 second timeout
)

def setup():
    if ser.isOpen():
        print(f"Serial port {ser.name} is open.")
        # Example: Send initial command to set motor speed and direction
        ser.write(b'S60\r')
        time.sleep(0.1)  # Small delay to allow the motor driver to process the command
    else:
        print(f"Failed to open serial port {ser.name}.")



def loop():
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting)
            print(f"Received data: {data.decode()}")
            

def main():
    try:
        
        
        # Example: Send specific commands to control the motor
         # Example command to set speed damping
        setup()
        loop()  # Enter loop to continuously monitor incoming data (optional)

    except KeyboardInterrupt:
        pass

    finally:
        if ser.isOpen():
            ser.close()
            print(f"Serial port {ser.name} is closed.")

if __name__ == '__main__':
    main()