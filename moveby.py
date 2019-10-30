# -*- coding: UTF-8 -*-
import csv
import cv2
import math
import os
import shlex
import subprocess
import tempfile

from olympe.messages.camera import start_recording
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
from olympe.messages.camera import start_recording, stop_recording
from olympe.messages import gimbal


import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
from olympe.messages.ardrone3.Piloting import moveBy
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
from olympe.messages.ardrone3.PilotingSettings import MaxTilt
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged
from olympe.messages.camera import recording_capabilities

import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
from pynput import keyboard
import time
from pynput.keyboard import Key, KeyCode, Listener
from pyparrot.Bebop import Bebop
from record import StreamingExample

drone = olympe.Drone("10.202.0.1")
drone.connection()


# create python file called autoPilot to write all the drone's movements
f = open("autoPilot.py", "w+")
# using f.write to the libraries to the autoPilot file
f.write("import olympe")
f.write("\n")
f.write("from olympe.messages.ardrone3.Piloting import TakeOff, Landing")
f.write("\n")
f.write("from olympe.messages.ardrone3.Piloting import moveBy")
f.write("\n")
f.write("from olympe.messages.ardrone3.PilotingState import FlyingStateChanged")
f.write("\n")
f.write("from olympe.messages.ardrone3.PilotingSettings import MaxTilt")
f.write("\n")
f.write("from olympe.messages.camera import start_recording, stop_recording")
f.write("\n")
# to connect to the simulated drone or the physical drone
# depends on the IP
# IP for the simulated drone '10.202.0.1'
# IP for the phusical drone '192.168.42.1'
f.write("drone = olympe.Drone('10.202.0.1')")
f.write("\n")
f.write("drone.connection()")
f.write("\n")


# take off function
def function_1():
    drone(
        TakeOff()
        >> FlyingStateChanged(state="hovering", _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
            >> f.write("    TakeOff()")
            >> f.write("\n")
            >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
            >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")

    )

# function to move the drone to the front
def function_2():
    drone(

        moveBy(1, 0, 0, 0)
        >> FlyingStateChanged(state='hovering', _timeout=5, _policy='check_wait', _float_tol=(1e-07, 1e-09))
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(1, 0, 0, 0)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")



    )



# function to move the drone back
def function_3():
    drone(
        moveBy(-1, 0, 0, 0)
        >> FlyingStateChanged(state='hovering', _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(-1, 0, 0, 0)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")
    )


# function to move the drone to the right
def function_4():
    drone(
        moveBy(0, 1, 0, 0)
        >> FlyingStateChanged(state='hovering', _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(0, 1, 0, 0)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")
    )

# function to move the drone to the left
def function_5():
    drone(
        moveBy(0, -1, 0, 0)
        >> FlyingStateChanged(state='hovering', _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(0, -1, 0, 0)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")
    )

# function to make rotation to the left
def function_6():
    drone(
        moveBy(0, 0, 0, -1)
        >> FlyingStateChanged(state='hovering', _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(0, 0, 0, -1)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")
    )


# function to make rotation to the right
def function_7():
    drone(
        moveBy(0, 0, 0, 1)
        >> FlyingStateChanged(state='hovering', _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(0, 0, 0, 1)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")
    )
# function to move the drone up
def function_8():
    drone(
        moveBy(0, 0, -1, 0)
        >> FlyingStateChanged(state='hovering', _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(0, 0, -1, 0)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")
    )
# function to move the drone down
def function_9():
    drone(
        moveBy(0, 0, 1, 0)
        >> FlyingStateChanged(state='hovering', _timeout=5)
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    moveBy(0, 0, 1, 0)")
        >> f.write("\n")
        >> f.write("    >> FlyingStateChanged(state='hovering', _timeout=5)")
        >> f.write("\n")
        >> f.write(").wait()")
        >> f.write("\n")
    )
# function to start recording from the drone's camera
def function_10():
    drone(
        start_recording(cam_id=0, _timeout=10, _no_expect=False, _float_tol=(1e-07, 1e-09))
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    start_recording(cam_id=0, _timeout=10, _no_expect=False, _float_tol=(1e-07, 1e-09))")
        >> f.write("\n")
        >> f.write(")")
        >> f.write("\n")
    )



# function to stop recording
def function_11():
    drone(
        stop_recording(cam_id=0, _timeout=10, _no_expect=False, _float_tol=(1e-07, 1e-09))
        >> f.write("drone(")
        >> f.write("\n")
        >> f.write("    stop_recording(cam_id=0, _timeout=10, _no_expect=False, _float_tol=(1e-07, 1e-09))")
        >> f.write("\n")
        >> f.write(")")
        >> f.write("\n")

    )




# function to land the drone and disconnect it
def function_12():
    drone(
       Landing()
       >> f.write("drone(Landing()).wait()")
       >> f.write("\n")
       >> f.write("drone.disconnection()")
       >> f.write("\n")
    ).wait()



#combination to functions

combination_to_function = {
    frozenset([KeyCode(char='T')]): function_1, # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([KeyCode(char='t')]): function_1,
    frozenset([KeyCode(char='W')]): function_2,
    frozenset([KeyCode(char='w')]): function_2,
    frozenset([KeyCode(char='S')]): function_3,
    frozenset([KeyCode(char='s')]): function_3,
    frozenset([KeyCode(char='D')]): function_4,
    frozenset([KeyCode(char='d')]): function_4,
    frozenset([KeyCode(char='A')]): function_5,
    frozenset([KeyCode(char='a')]): function_5,
    frozenset([KeyCode(char='Q')]): function_6,
    frozenset([KeyCode(char='q')]): function_6,
    frozenset([KeyCode(char='E')]): function_7,
    frozenset([KeyCode(char='e')]): function_7,
    frozenset([KeyCode(char='U')]): function_8,
    frozenset([KeyCode(char='u')]): function_8,
    frozenset([KeyCode(char='N')]): function_9,
    frozenset([KeyCode(char='n')]): function_9,
    frozenset([KeyCode(char='C')]): function_10,
    frozenset([KeyCode(char='c')]): function_10,
    frozenset([KeyCode(char='V')]): function_11,
    frozenset([KeyCode(char='v')]): function_11,
    frozenset([KeyCode(char='L')]): function_12,
    frozenset([KeyCode(char='l')]): function_12,


}

# Currently pressed keys
current_keys = set()

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
    current_keys.remove(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



drone(Landing()).wait()
drone.disconnection()

# disconnect the drone in the autoPilot file
f.write("drone(wait())")
f.write("drone(Landing()).wait()")
f.write("\n")
f.write("drone.disconnection()")
f.write("\n")
