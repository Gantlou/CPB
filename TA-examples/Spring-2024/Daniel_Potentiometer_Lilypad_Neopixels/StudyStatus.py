# Daniel Giganti Dima 3/3/24 AoM Wearables Demo

# Import stuff
# include
import board
import analogio
import digitalio
import neopixel  # import neopixel module to access neopixels
import time
from time import sleep  # import sleep function from time module
Red = 255
Green = 255
Blue = 0
PotColor = (Red, Green, Blue)

# Set potentiometer values
readInValue = analogio.AnalogIn(board.A1)  # og pot value

# Set up button
button = digitalio.DigitalInOut(board.D9)
button.switch_to_input(pull=digitalio.Pull.DOWN)
buttonState = button.value

# Setup neopixel
extNeo = neopixel.NeoPixel(
    board.D10, 1, brightness=0.5
)  # extNeo is the external neopixels connected to Bluefruit on pin D10

def theaterChase(pixels, color, wait):
    """Sequantially set pixels RGB values equal to color,
    # then to off at interval specified by wait"""
    pixels[0] = color
    sleep(wait)

# Actually running it
while True:
    potvalue = (readInValue.value * 3.3) / 65536    # converts analog voltage to 0-3.3 [Volt]
    print(potvalue)
    count = 0
    if button.value == 1:
        while count <= 5:
            Red = 255
            Green = 0
            Blue = 0
            theaterChase(extNeo, ((Red, Green, Blue)), 0.001)
            sleep(0.1)
            theaterChase(extNeo, ((0, Green, Blue)), 0.1)
            count += 1
    # flash led to tell person to go away
    else:
        # business as usual
        # Define when red, green, and yellow/orange are shown on the potentiometer
        if potvalue < 1.0 and potvalue >= 0.0:
            # Convert analog to 3.3V value (for better understanding)

            Red = 255
            Green = 0
            Blue = 0
            theaterChase(extNeo, ((Red, Green, Blue)), 0.001)
            sleep(0.001)
        elif potvalue >= 1.0 and potvalue < 2.2:
            Red = 255
            Green = 255
            Blue = 0
            theaterChase(extNeo, ((Red, Green, Blue)), 0.001)
            sleep(0.001)
        else:
            Red = 0
            Green = 255
            Blue = 0
            theaterChase(extNeo, ((Red, Green, Blue)), 0.001)
            sleep(0.001)
    time.sleep(0.01)
