## Exam Stress | Pulse Sensor and Onboard Neopixels

### Use case:
You are studying for an exam and feel yourself starting to get stressed.


### What it does: 
The Onboard Neopixels flash red when the heart rate monitor detects a heart rate of 80 BPM or higher. The onboard Neopixels turn green when a heart rate below 80 BPM is detected


### How it works: 
The system has one main input: Adafruit heart rate monitor, the heart rate monitor detects a signal that will output an analog signal to the Bluefruit. This signal is then converted into serial data in the Bluefruit so it can output the corresponding light on the Neopixels.

The system has one main output: on-board Neopixels, If pin A4 reads a heartrate the onboard Neopixels will flash or turn on to their respective colors red, or green. 


### Demo Video: 
https://youtu.be/2TnVhYituzw)https://youtu.be/2TnVhYituzw
