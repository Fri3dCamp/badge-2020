# ESP32 Micropython firmware
This firmware is taken from st7789_mpy project and has been included here for convenience.

## Getting Started
Figure out what the port of your badge is.

On Mac, this is something like `/dev/tty.usbserial-xxxxxxxx`

1. Erase the flash
```shell
esptool.py --chip esp32 --port $PORT erase_flash
```

2. Flash the firmware
```shell
esptool.py --chip esp32 --port $PORT write_flash -z 0x1000 $FIRMWARE_DIR/firmware.bin
```
