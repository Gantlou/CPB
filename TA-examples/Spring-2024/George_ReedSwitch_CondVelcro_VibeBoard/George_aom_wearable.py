# Author: George Spann, Last modified 03/04/2024
# reed switch, vibe board, conductive velcro

# import necessary libraries first
import board  # board: used to communicate with the CPB board
import digitalio  # digitalio: used to configure CPB GPIO Pins
import touchio  # import touch functionality
import neopixel #import neopixel

# initialize digital output to vibe board, on pin D10
vibe = digitalio.DigitalInOut(board.D10)
vibe.direction = digitalio.Direction.OUTPUT

# initialize reed switch as an input
switch = digitalio.DigitalInOut(board.D9)
switch.switch_to_input(pull=digitalio.Pull.DOWN)

# initialize conductive velcro and onboard neopixels
onboard = neopixel.NeoPixel(board.D8, 10, brightness=.5)
velcro_pad = board.A4
velcro = touchio.TouchIn(velcro_pad)


# setting up vibration board (vibe board) to buzz
while True:
    if (switch.value == False) and (velcro.value == False):
        vibe.value = True
        onboard.fill((0, 255, 0))  # change onboard neopixels to green color
    elif (switch.value == True) and (velcro.value == False):
        vibe.value = False
        onboard.fill((0, 255, 0))  # change onboard neopixels to green color
    else:
        vibe.value = False
        onboard.fill((0, 0, 0))  # turn off neopixels
