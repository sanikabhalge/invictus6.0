import Jetson.GPIO as GPIO
import time

# Pin Definitions
output_pin = 29 # BCM pin 18, BOARD pin 12

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    mode=GPIO.getmode()
    print(mode)
    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            time.sleep(1)
            # Toggle the output every second
            print("Outputting {} to pin {}".format(curr_value, output_pin))
            GPIO.output(output_pin, curr_value)
            curr_value ^= GPIO.HIGH
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()




""" this is the code used for running 2 mosfet with common ground for indicator lights"""
import Jetson.GPIO as GPIO
import time

# Pin Definitions
output_pin_1 = 15  # BCM pin 18, BOARD pin 12 (blue light) 
output_pin_2 = 32  # (green light)

def main():
    # Pin Setup
    print("Initializing GPIO...")
    GPIO.setmode(GPIO.BOARD)  # Use BOARD pin-numbering scheme
    GPIO.setup(output_pin_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin_2, GPIO.OUT, initial=GPIO.LOW)

    mode = GPIO.getmode()
    print(f"Current GPIO mode: {mode}")
    print("Starting demo now! Press CTRL+C to exit.")

    try:
        while True:
            try:
                ask_user = int(input("Select an option:\n1. MOSFET 1 on for 2 sec\n2. MOSFET 2 on for 2 sec\n3. Both MOSFETs on for 2 sec\nYour choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            # Turn off both outputs before processing input
            GPIO.output(output_pin_1, GPIO.LOW)
            GPIO.output(output_pin_2, GPIO.LOW)

            if ask_user == 1:
                print("Activating blue light.")
                GPIO.output(output_pin_1, GPIO.HIGH)
                GPIO.output(output_pin_2, GPIO.LOW)
                time.sleep(2)  # Keep it on for 2 seconds
            elif ask_user == 2:
                print("Activating green light.")
                GPIO.output(output_pin_2, GPIO.HIGH)
                GPIO.output(output_pin_1, GPIO.LOW)
                time.sleep(2)  # Keep it on for 2 seconds
            elif ask_user == 3:
                print("Activating both lights.")
                GPIO.output(output_pin_1, GPIO.HIGH)
                GPIO.output(output_pin_2, GPIO.HIGH)
                time.sleep(2)  # Keep them on for 2 seconds
            else:
                print("Exiting program.")
                GPIO.output(output_pin_1, GPIO.LOW)
                GPIO.output(output_pin_2, GPIO.LOW)
                break

    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
