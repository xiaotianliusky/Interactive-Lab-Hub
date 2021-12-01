import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import random
import qwiic_joystick
import sys

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
DARKRED   = (155,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font_time = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

play = False
directions = {0: "left", 1:"straight", 2:"right", 3:"up", 4:"down"}
joy = qwiic_joystick.QwiicJoystick()
joy.begin()
joydefault = [521, 506]
message = "Press a button to play!"
score = 0
def checkUp(vals):
    if vals[0] < joydefault[0]:
        return True
    return False
def checkLeft(vals):
    if vals[1] > joydefault[1]:
        return True
    return False
def checkDown(vals):
    if vals[0] > joydefault[0]:
        return True
    return False
def checkStraight(vals):
    return True
def checkRight(vals):
    if vals[1] < joydefault[1]:
        return True
    return False
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    if (not buttonA.value) or (not buttonB.value):
        play = True
    if play:
        direction = directions[random.randint(0,4)]
        draw.text((100, 50), direction, font=font, fill="#ffffff")
        disp.image(image, rotation)
        time.sleep(1)

        
        if direction == LEFT:
            if not checkLeft([joy.horizontal, joy.vertical]):
                play = False
                message = "Sorry you lost:( Score: " + str(score)
                score = 0
        elif direction == RIGHT":
            if not checkRight([joy.horizontal, joy.vertical]):
                play = False
                message = "Sorry you lost:( Score: " + str(score)
                score = 0
        elif direction == UP:
            if not checkUp([joy.horizontal, joy.vertical]):
                play = False
                message = "Sorry you lost:( Score: " + str(score)
                score = 0
        elif direction == DOWN:
            if not checkDown([joy.horizontal, joy.vertical]):
                play = False
                message = "Sorry you lost:( Score: " + str(score)
                score = 0
        score = score + 1
    else:
        draw.text((10, 50), message, font=font, fill="#ffffff")
        disp.image(image, rotation)
