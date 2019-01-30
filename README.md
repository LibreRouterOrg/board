# librerouter

LibreRouter.org source router repo.

## Description

![librerouter actual photo](https://raw.githubusercontent.com/libremesh/librerouter/master/designs/photos/prototipe_phase2.jpg)

You will find two boards in the design/ folder:
* core: contains all the more integrated components, namely: cpu, memory, storage, watchdog. Facilitates the access to the pinouts of the cpu and keeps all the most integrated circuitry in one board.
* mega board: contains the peripheral connectors.

This hardware works great with the libremesh.org software.

More photos can be downloaded from http://downloads.libremesh.org/librerouter/librerouter_pics_core-v0.2_mega-v1.zip

## Quick Specs
| Element | Description |
| --- | ---- |
| SOC|   QCA9558       |
| RAM|   128M DDR2     | 
| Flash| 16MiB SPI-NOR |
| ETH|   QCA8337N 2x 10/100/1000 PoE and PoE pass-through |
| WiFi2| QCA9558 (bgn) 2T2R |
| WiFi5| 2x mPCIE with AR9582 (an) 2T2R |
| BTN |  1x Reset |
| GPIO|  multiple GPIO on header, PoE passthrough enable |
| UART|  3.3V 115200N8 header on the board |
| WDG |  ATTiny13 watchdog |
| JTAG|  header on the board |
| USB |  1x connector and 1x header on the board |
| PoE |  10-32V input in ETH port 1, passthrough in port 2 |
| GPS |  with PPS |
| mPCIE | 2x populated (but replaceable with compatible mPCIE board) |
