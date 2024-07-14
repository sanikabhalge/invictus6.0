import time
from my_mcp4725 import MCP4725

# Initialize the MCP4725 DAC at address 0x60
dac = MCP4725(address=0x60)

while True:
    print("0")
    dac.setVoltage(1228)
    # time.sleep(5)
    # print("Setting voltage to 2078")
    # dac.setVoltage(1236)
    # time.sleep(5)
    # print("Setting voltage to 4095")
    # dac.setVoltage(4095)
    # time.sleep(5)