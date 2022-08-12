# Fri3dcamp Micropython firmware
This firmware is compiled from https://github.com/Fri3dCamp/Badge2020_micropython and has been included here for convenience.

The .bin files are in the zip file.

## Getting Started
Figure out what the port of your badge is.

On Mac, this is something like `/dev/tty.usbserial-xxxxxxxx`

```shell
export PORT=/dev/ttyUSB0
```

1. (optional) Erase the flash
```shell
esptool.py --chip esp32 --port $PORT erase_flash
```

2. Flash the firmware
```shell
esptool.py --chip esp32 -p $PORT -b 460800 --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 40m --flash_size 16MB 0x1000 bootloader.bin 0x10000 micropython.bin 0x8000 partition-table.bin

```
