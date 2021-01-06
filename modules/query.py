import subprocess
import re

def Devices():
    #get output
    output = subprocess.check_output(["scanimage", "-L"])
    #parse output
    devices = re.findall("`.*'", output)
    return devices

# Inputs: deviceID (str) from Devices() ex: "pixma:04A926EF_SJ3029112970S)
# Return dict:
#   ['resolution', 'mode']
def Capabilities(deviceID):
    #get output
    output = subprocess.check_output(["scanimage", "--help", "-d", deviceID])
    #parse output
    resolutionstr = re.findall("--resolution (.*)dpi [", output)
    modestrt = re.findall("--mode (.*) [", output)
    resolution = []
    mode = []
    #set output
    dict = {
        'resolution': resolution,
        'mode': mode,
    }
    return dict
def I2c():

    return
def UsbID(VendorID):
    return
