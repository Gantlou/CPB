## VibraFlag | Conductive Velcro, Reed Switch, Vibe Motor, Onboard Neopixels

### Use case: This is a demo of a wearable device that gives you immediate feedback when your flag is pulled during a game of flag football.



### What it does: The system uses conductive velcro to integrate into the user's jersey. When the flag with a sewn in magnet is pulled out of the user's pocket this triggers the reed switch on the wearable. The Bluefruit  sends a signal to the vibe motor, turning it on, indicating to the user that the flag was pulled.



### How it works: The system has 2 main inputs: the conductive velcro and the reed switch.

### The Conductive Velcro is configured as an analog input, with one piece of the velcro receiving 3.3V from the CPB and the other piece being connected to ground through a pull-down resistor. When a stand alone piece of velcro, sewn into the user's cloths is used to bridge these other two pieces of velcro it completes the circuit, allowing the wearable to function. 

### The reed switch is configured such that one end is receiving 3.3V and the other end is tied to ground via a pull-down resistor. While the magnet in the flag is within close proximity the reed switch acts as a complete wire essentially and completes the circuit the CPB reads this 'high' signal in and does nothing. When the flag is pulled and the magnetic field is no longer acting on the reed switch the circuit is effectively broken sending a 'low' signal to Bluefruit, and ultimately setting off the vibe motor.

### The system has 2 main outputs: the Vibe Motor and Onboard Neopixels.

### The vibe motor is an output device. It is connected to pin A3. When the Bluefruit reads in a 'TRUE' value from the reed switch circuit a 'FALSE' will be sent to pin A3. The opposite is also true, A 'FALSE' from the reed switch will result in a 'TRUE' value being sent to the vibe motor (consequently turning it on).

### The Onboard neopixels are built-in to the CPB and configured using an onboard I/O initialization. These are given a green  RGB value to indicate what color to illuminate.


### Peripherals:

**Digital Inputs:**
## 
**Digital Outputs:**
## Onboard Neopixels
**Analog Inputs:**
## Conductive Velcro, Reed Switch
**"Analog" (PWM) Outputs:**
## Vibe Motor

**Serial Communication:**

### Demo Video: https://www.youtube.com/watch?v=jw04MeYGr2s
