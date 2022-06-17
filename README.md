# RSCalibration

This repository documents practical methods to estimate [rolling shutter](https://en.wikipedia.org/wiki/Rolling_shutter) readout times.

Software such as [ODM](https://github.com/OpenDroneMap/ODM) can compensate for the rolling shutter effect when a set of photos is captured in motion, but knowledge of the sensor readout time is necessary to perform this correction.

We present below an inexpensive method to build a calibration device using an Arduino:

![image](https://user-images.githubusercontent.com/1951843/174381801-bb0e3c9f-6aa4-43dd-bf72-7c10b16fa231.png)

![image](https://user-images.githubusercontent.com/1951843/174384049-ac5dcfea-db4b-4f8d-b3f2-5263bedd11e9.png)

The idea is to blink an LED at ~2khz, capture a photo using a fast shutter speed and count the number of lines in the result. Each line will represent ~1ms of time, thus the total readout time will be close to: `number of lines ~= readout time (ms)`.

## Required hardware

Most of these items can be found on eBay, or electronics retailers like Sparkfun.

 - [x] 1x Arduino-compatible board
 - [x] 1x 80Ω (or less) resistor
 - [x] 1x LED
 - [x] 1x breadboard (not strictly required, but makes wiring easier)
 - [x] 2x 22AWG jump wires (not strictly required, but makes wiring easier)

## Schematics

![image](https://user-images.githubusercontent.com/1951843/174387902-d1ec32e7-31cf-4460-b311-fc2d58248f85.png)

## Code

You can upload the following code to the Arduino board and change the `ledPin` variable if needed. Choose a digital output pin:

 - [blink.ino](https://github.com/OpenDroneMap/RSCalibration/blob/main/blink.ino)

## Procedure

1. Turn on the Arduino device
2. Place the camera on a stable surface close to the LED
3. Take a picture of the LED using the **fastest shutter speed setting available**
4. Examine the picture and count the total number of lines (both dark and colored lines). For example, the picture below has ~25 lines and the estimated readout time is thus `25ms`:

![image](https://user-images.githubusercontent.com/1951843/174388401-09e18fee-1975-43fa-8f56-6f5d046fe475.png)

5. Use the form at https://opendronemap.github.io/RSCalibration/ to contribute to [ODM's database of rolling shutter cameras](https://github.com/OpenDroneMap/ODM/blob/master/opendm/rollingshutter.py).
