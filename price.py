#!/usr/bin/env python
#
# !!! Needs psutil (+ dependencies) installing:
#
#    $ sudo apt-get install python-dev
#    $ sudo pip install psutil
#

from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont


def stats(oled):
    font = ImageFont.load_default()
    font2 = ImageFont.truetype('C&C Red Alert [INET].ttf', 14)
    with canvas(oled) as draw:
        draw.text((0, 0), "Channel " , font=font2, fill=255)
        draw.text((0, 18), "Item ", font=font2, fill=255)
        draw.text((0, 32), "Price ", font=font2, fill=255)
        #draw.text((0, 38), network('wlan0'), font=font2, fill=255)

def main():
    oled = ssd1306(port=0, address=0x3C)
    stats(oled)

if __name__ == "__main__":
    main()
