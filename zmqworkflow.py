import datetime
import zmq
import random
import time
import RPi.GPIO as GPIO

def log(message):
   currentDT = datetime.datetime.now()
   print (str(currentDT) + " " + message)

import pygame

pygame.mixer.init()
pygame.mixer.music.load("mp3/intercom.mp3")

log("zmq-workflow started")

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:24001")
socket.setsockopt(zmq.SUBSCRIBE, b'motion')

while True:
    [topic, time] = socket.recv_multipart()
    #message = socket.recv()
    print("Motion received : " + time)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        pass

