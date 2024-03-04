## CPB TA Demo - StudyStatus | Potentiometer, Off-board Lilypad Button, Off-board Neopixel

### Use case: This is a demonstration of a system to display your availability to talk to or help someone when you're preoccupied.


### What it does: 

The system displays the colors red, yellow, and green on an off-board neopixel to "set your status" and show others whether you're available to talk, busy but can pause, or unavailable whatsoever respectively. The off-board button flashes the neopixel red 5 times to bring your status to someone's attention if they do not initially see your red status.


### How it works: 

The potentiometer is an "analog" (PWM) input connected to pin A1, 3.3V, and GND. The status is set by moving the dial on a potentiometer, which is set to evenly represent the three colors/statuses from 0 to 3.3 volts.  As you move the dial back and forth, you change the amount of resistance, and therefore the voltage that is input to the Bluefruit, which converts the voltage to a value between 0 and 65535, which is then converted to a value between 0 and 3.3 volts. This is then split into bins to determine the color of the neopixel. 

The neopixel is connected to 3.3V, GND, and pin D10 as a digital output. It is given an RGB value to know what color to illuminate depending on when the button is pressed or what value the potentiometer is at.

There is a pull-down resistor connected to A2 and GND, with the off-board button between A2 and the resistor. The other side of the button is connected to 3.3V to complete the circuit.

### Peripherals:

**Digital Inputs:** Lilypad Button

**Digital Outputs:** Offboard Neopixel

**"Analog" (PWM) Outputs:** Potentiometer

### Demo Video: 
https://youtu.be/NjA_apPVIT0

