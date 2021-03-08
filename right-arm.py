#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# TODO: Add code here

ts = TouchSensor()
leds = Leds()

leds.set_color("LEFT", "GREEN")
leds.set_color("RIGHT", "GREEN")
sound = Sound()
sound.speak('Gorilla move right arm')

m = LargeMotor(OUTPUT_D)
m.on_for_rotations(SpeedPercent(10),0.2)
m.on_for_rotations(SpeedPercent(-10),0.2)


leds.set_color("LEFT", "RED")
leds.set_color("RIGHT", "RED")

sleep(0.01)
