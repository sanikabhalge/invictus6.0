# adafruit_mcp4725.py

import board
import busio
from adafruit_mcp4725 import MCP4725 as Adafruit_MCP4725

class MCP4725:
    def __init__(self, address=0x60):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.dac = Adafruit_MCP4725(self.i2c, address=address)
    
    def setVoltage(self, voltage):
        "Sets the output voltage to the specified value (0-4095)"
        if voltage < 0:
            voltage = 0
        if voltage > 4095:
            voltage = 4095
        self.dac.raw_value = voltage
