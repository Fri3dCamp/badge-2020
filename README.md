# Fri3d Badge 2020

This repository contains the hardware design of the [Fri3d Camp](https://fri3d.be/) badge for 2020 / 2022. The project progress can be followed on our [Hackaday.io](https://hackaday.io/project/169741-fri3d-2022-badge) page.

## Blockdiagram

In order to make the documentation easier to use, we've added the block diagram in this repository.

![Badge Block Diagram](media/Badge_Block.png)

## REV 00
First prototype to verify the schematic design.

![Badge 00](media/Badge_00.jpg)

## REV 01
Moved away from the Adafruit Feather compatible expansion header in favor for the [BBC micro:bit expansion connector](https://tech.microbit.org/hardware/edgeconnector/)

![Badge 01](media/Badge_01_BACK_noBG.png)

![Badge 01 GameOn](media/Badge_01_GameOn.jpg)
Test fit of the badge with the first protoype of the [GameOn](https://github.com/Fri3dCamp/gameon-2020)


## REV 02
Upgraded the micro:bit connector to V2 shape.
This board has the final shape for the badge and has a green soldermask with black silkscreen.

![Badge 02 Close up](media/Badge_02_Closeup.jpg)

![Badge 02 Close up](media/Badge_02_Front.jpg)

![Badge 02 Close up](media/Badge_02_Back.jpg)


## REV 03
The production version of the badge with improvements in the BadgeLink circuit and a change in the LCD backlight button operation. Now the slide switch will either turn the display backlight ON or render it's control to the interrupt pin from the accelerometer allowing for wakeup based on movement for increased battery savings.

## Documentation
In the "media" folder we've added the small infosheet leaflet that's included with the badge.

![Badge 03 info front](media/Info_front.png)

![Badge 03 info rear](media/Info_rear.png)