import serial
import time

# Configure the UART port
uart_port = '/dev/ttyUSB0'  # Change this to your UART port
baud_rate = 9600  # Set baud rate

# Initialize serial communication
ser = serial.Serial(uart_port, baud_rate, timeout=1)

try:
    # Give some time for the connection to establish
    time.sleep(2)

    while True:
        msg = input("enter: ")
        ser.write((msg + '\n').encode())
        print(msg)
        time.sleep(2)  # Wait before sending again

except Exception as e:
    print("Error:", e)

finally:
    # Close the UART connection
    ser.close()

