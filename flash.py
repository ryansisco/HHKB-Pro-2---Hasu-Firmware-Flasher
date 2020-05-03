import os
import sys
import time


try:
	firmware = sys.argv[1]
except:
	firmware = input("firmware to flash?: ")

choice = input("Flash HHKB Pro 2 with " + firmware + "?(y/n): ")
if (choice != "y"):
	print("Quitting")
	exit(1)
print("Please place device into recovery/boot mode within the next 15s")
for i in range(15):
	print(15-i)
	time.sleep(1)


print("\n\t\t**ERASING**\n")
os.system("dfu-programmer atmega32u4 erase --force")
print("\n\n\n\t\t**FLASHING with " + sys.argv[1] + "**\n")
os.system("dfu-programmer atmega32u4 flash " + sys.argv[1])
print("\n\n\n\t\t**RESETTING**")
os.system("dfu-programmer atmega32u4 reset")