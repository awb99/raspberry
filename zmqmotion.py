import datetime
import zmq
import random
import time
import RPi.GPIO as GPIO


def log(message):
   currentDT = datetime.datetime.now()
   print (str(currentDT) + " " + message)


log("zmq-motion started. zmqPUB port: 24001")

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:24001")

# https://pi4j.com/1.2/pins/model-3b-rev1.html#Numbering_Scheme
# I use The BOARD config, so 1-40
# configuration of motion detector:
# http://henrysbench.capnfatz.com/henrys-bench/arduino-sensors-and-input/arduino-hc-sr501-motion-sensor-tutorial/

# edge detection:
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/


print(GPIO.RPI_INFO)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
cMotion=38
GPIO.setup(cMotion, GPIO.IN)

while True:
    if GPIO.input(cMotion):
        log("Motion Detected...")
        currentDT = datetime.datetime.now()
        # socket.send_string("motion" + str(currentDT))
        socket.send_multipart([b"motion" , str(currentDT)])
        time.sleep(3) # after detecting sleep 3 secs to not re-generate the same signal
    else:
        time.sleep(0.25)

log("zmq-motion stopped")

