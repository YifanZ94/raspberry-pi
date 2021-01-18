# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:15:58 2021

@author: Administrator
"""

# Imports the necessary libraries...
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
font = ImageFont.truetype("/usr/share/fonts/truetype/piboto/PibotoLt-Regular", 15)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/piboto/PibotoLt-Regular", 30)

i2c = board.I2C()
RESET_PIN = digitalio.DigitalInOut(board.D26)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D,reset=RESET_PIN)
#
class SSD:
    def __init__(self):
        self.oled = oled
    
    def display(self,loc):
        oled.fill(0)
        oled.show()
        # create blank image for drawing
        self.image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        # draw
        self.draw.text((0, 0), "location", font=font,fill=255)
        self.draw.text((0,30), "{}".format(loc), font=font2, fill=255)
        # display
        self.oled.image(self.image)
        self.oled.show()

