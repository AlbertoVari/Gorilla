# Gorilla
Jetson Nano machine learning project to control robot with gesture recognition based on TSM model

Gorilla project is an application of TSM: Temporal Shift Module https://github.com/mit-han-lab/temporal-shift-module machine learning running on Jetson NANO and remote control of Lego EV3 robot with gesture recognition.

-Swiping Right moves EV3 right arm
-Swiping Left moves EV3 left arm

Hardware requirements :

NVIDIA Jetson NANO
LEGO EV3 Robot
USB Camera

Software requirements :

pip3 install onnx-simplifier==0.2.18

export PATH=/usr/local/cuda-10.2/bin:$PATH

check USB camera on /dev/video0 : ls -ltrh /dev/video*

pi3 install paramiko http://www.paramiko.org/

install https://www.ev3dev.org/ on EV3 robot
