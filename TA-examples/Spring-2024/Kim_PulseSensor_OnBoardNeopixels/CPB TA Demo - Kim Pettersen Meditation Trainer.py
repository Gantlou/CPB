#Edited Spring 2024 by Kim Pettersen for The Art of Making
#Based on code from Jam On!

import time
import board
import board  # import board module to access board's pins
import neopixel  # import neopixel module to access neopixels
import analogio
import digitalio


# Onboard Neopixels
onboard = neopixel.NeoPixel(board.NEOPIXEL,10,brightness=.2)

# Red LEDs
led = digitalio.DigitalInOut(board.D9)
led.direction = digitalio.Direction.OUTPUT

# Color Button Switch
color_button = digitalio.DigitalInOut(board.A4)
color_button.switch_to_input()
#color_button = analogio.AnalogIn(board.A4)

# Pot
pot = analogio.AnalogIn(board.A6)

MIN_ANALOG_VOLTAGE = 1000
MAX_ANALOG_VOLTAGE = 65535
color = 0

# HR Sensor
pulseSensor = analogio.AnalogIn(board.A5)  # set up to read sensor
onboard[1]=(0, 100, 0)

OFF=0
ON=2**15  #2^15

sampleCounter = 0  # tracks pulse timing
lastBeatTime = 0  # find IBI
IBI = 600  # hold time interval between beats must give an initial value first
Pulse = False  # is True wen a heartbeat is detected
QS = False  # is true when a beat is found
P = 512  # find the peak
T = 512  # find the trough
globalthresh=700 #edit this to adjust the thresh for testing
thresh = globalthresh  # find instant amount of beat (may need to tweak this)
amp = 0  # amplitude of pulse
firstBeat = True  # if its the first beat
secondBeat = False  # if its the second beat
rate = [0,0,0,0,0,0,0,0,0,0]

#mapping analog values from bluefruit to the range of arduino to shove arduino code into python :(
low2=0
high2=1023 #high analog value from arduino
low1=0
high1=65535 #high analog value from bluefruit

BPM = 0

def mapper(val):
    val = low2+(val-low1)*(high2-low2)/(high1-low1)
    return val

def redNeos():
    strip.fill((255, 0, 0))
    onboard.fill((255, 0, 0))

def greenNeos():
    strip.fill((0, 255, 0))
    onboard.fill((0, 255, 0))

def blueNeos():
    strip.fill((0, 0, 255))
    onboard.fill((0, 0, 255))

def offNeos():
    strip.brightness = .01
    onboard.brightness = .01

def onNeos():
    brightness_level = num_to_range(pot.value, MIN_ANALOG_VOLTAGE, MAX_ANALOG_VOLTAGE, 0.1, 0.5)
    strip.brightness = brightness_level
    onboard.brightness = brightness_level


def flashRed(settime, numTimes):
    neopixel.brightness = .2
    redNeos()
    for i in range(0, numTimes):
        led.value = True
        onNeos()
        time.sleep(settime)
        led.value = False
        offNeos()
        time.sleep(settime)

def num_to_range(num, inMin, inMax, outMin, outMax):
    return (outMin + (float(num - inMin) / float(inMax - inMin) * (outMax - outMin)))

#filter noise from pulseSensor
while True:
    time.sleep(.003)
    Signal= mapper(pulseSensor.value)

    sampleCounter += 2
    N=sampleCounter-lastBeatTime
    if Signal < thresh and N > (IBI/5)*3:
        if Signal < T:
            T=Signal

    if Signal > thresh and Signal > P:
        P=Signal


    if N>300:  # avoid high freq noise only get pulses

        if ((Signal > thresh) and (Pulse is False) and (N > (IBI/5)*3)):
            Pulse= True  # there is a pulse!

            onNeos()
            # print(Signal)

            # add in output like a light or sound
            IBI = sampleCounter - lastBeatTime  # measure time between beats
            lastBeatTime = sampleCounter

            if firstBeat:  # on the first beat
                firstBeat = False
                secondBeat = True
            else:
                if secondBeat:  # on the second beat
                    secondBeat = False
                    for i in range(10):
                        rate[i] = IBI  # seed the running total to get a BPM at start

                # now we find running total of last 10 IBI vals
                runningTotal = 0  # clear total

                for i in range(9):
                    rate[i]=rate[i+1] # shift data in rate and drop lowest
                    runningTotal += rate[i]
                rate[9] = IBI  # add latest IBI
                runningTotal += rate[9]  # add IBI to total
                runningTotal /= 10  # find avg
                BPM = 60000 / runningTotal
    if (Signal < thresh and Pulse is True):  # values are going down so beat is over
        # turn off your light or sound
        Pulse = False

        offNeos()    # Turn LED off

        amp = P - T  # get amp of wave
        thresh = amp/2 + T  # set thresh at 50% of amp
        P = thresh  # reset peak and trough for next wave
        T = thresh

    if N > 2500:  # if 2.5 sec go without beat
        thresh = globalthresh
        P = 512
        T = 512
        lastBeatTime = sampleCounter
        firstBeat = True
        secondBeat = False

    print(BPM)


    if(BPM > 80):
        flashRed(0.1, 20)
        BPM = 0

    else:
        greenNeos()
        BPM = 0
