# RSCalibration

This repository documents practical methods to estimate [rolling shutter](https://en.wikipedia.org/wiki/Rolling_shutter) readout times.

Software such as [ODM](https://github.com/OpenDroneMap/ODM) can compensate for the rolling shutter effect when a set of photos is captured in motion, but knowledge of the sensor readout time is necessary to perform this correction.

We present below an inexpensive method to build a reader device using an Arduino:

![image](https://user-images.githubusercontent.com/1951843/174381801-bb0e3c9f-6aa4-43dd-bf72-7c10b16fa231.png)

![image](https://user-images.githubusercontent.com/1951843/174392415-d2aee736-ed5a-4c93-83ca-0ac3eb5f9425.png)

The idea is to blink an LED at ~2khz, capture a photo using a fast shutter speed and count the number of lines in the result. Each line will represent ~1ms of time, thus the total readout time will be close to: `number of lines ~= readout time (ms)`.

## Required hardware

Most of these items can be found on eBay, or electronics retailers like Sparkfun.

 - [x] 1x Arduino-compatible board
 - [x] 1x 80Ω (or less) resistor
 - [x] 1x LED
 - [x] 1x breadboard (not strictly required, but makes wiring easier)
 - [x] 2x 22AWG jump wires (not strictly required, but makes wiring easier)

## Schematics

![image](https://user-images.githubusercontent.com/1951843/174392464-3da5045b-e83d-4d80-a1fd-efc9d8023ff9.png)

## Code

You can upload the following code to the Arduino board and change the `ledPin` variable if needed. Choose a digital output pin:

 - [blink.ino](https://github.com/OpenDroneMap/RSCalibration/blob/main/blink.ino)

## Procedure

1. Turn on the Arduino device
2. Place the camera on a stable surface close to the LED
3. Take a picture of the LED using the **fastest shutter speed setting available**
4. Examine the picture and count the total number of lines (both dark and colored lines). For example, the picture below has ~25 lines and the estimated readout time is thus `25ms`:

![image](https://user-images.githubusercontent.com/1951843/174392533-429943a6-82b2-4948-9637-3cb35fd21707.png)

## No-Tinker Solution

### Required Hardware

 - [x] Raspberry Pi Pico (RP2040)-compatible board
 ![image](https://user-images.githubusercontent.com/19295950/175455634-6be7e3cd-9abe-4260-8af0-7bab0909fb67.png)
 
### Schematics

You will only need to connect your RP2040 board to your computer for programming using whatever cable/interface your board has (microUSB, Type-C, etc)

### Code

You can upload the following MicroPython code to the RP2040-compatible board using Thonny:  
 - [main.py](https://github.com/OpenDroneMap/RSCalibration/blob/main/main.py)

```python
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=1000, mode=Timer.PERIODIC, callback=blink)
```

![image](https://user-images.githubusercontent.com/19295950/175456447-7df30e7e-4034-43b4-8cb1-95d51fa1c1a4.png)

1. Plug in your RP2040-compatible board while hoading the Bootsel button. It will show up as a removeable-storage drive
2. Set Thonny to use the MicroPython Interpreter under Options -> Interpreter
3. Upload the latest MicroPython firmware to the RP2040-compatible board
4. After the board reboots, open main.py with Thonny and save it to the RP2040-compatible board as main.py

### Procedure

1. Same data collection procedure as above

## Contribute to ODM

You can use the form at https://opendronemap.github.io/RSCalibration/ to contribute to [ODM's database of rolling shutter readout times](https://github.com/OpenDroneMap/ODM/blob/master/opendm/rollingshutter.py).
