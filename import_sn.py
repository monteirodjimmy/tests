import os, sys
import subprocess

var = str(subprocess.call(['sudo', 'dmidecode', '-s', 'system-serial-number' ]))
print (var)




"""
def getMachine_addr():
    
    os_type = sys.platform.lower()

    if "darwin" in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
    elif "win" in os_type:
        command = "wmic bios get serialnumber"
    elif "linux" in os_type:
        command = "dmidecode -s baseboard-serial-number"
    return os.popen(command).read().replace("\n", "").replace("  ", "").replace(" ", "")
print("Your motherboard Serial No.", getMachine_addr())
"""

