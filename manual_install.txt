These are the commands issued during the flash (taken from TMK documentation)

dfu-programmer atmega32u4 erase --force
dfu-programmer atmega32u4 flash <your_firmware.hex>
dfu-programmer atmega32u4 reset


simply run the program, or enter the name of your firmware to flash at the end of the script name

"python ./flash.py"
"python ./flash.py myfirware.hex"

