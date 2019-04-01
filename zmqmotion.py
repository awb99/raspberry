import datetime
import zmq
import random
import time

def log(message):
   currentDT = datetime.datetime.now()
   print (str(currentDT) + " " + message)


log("zmq-motion started. zmqPUB port: 24001")

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:24001")

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print(str(topic) + " " + str(messagedata))
    socket.send_string(str(topic) + " " + str(messagedata))
    time.sleep(5)


log("zmq-motion stopped")

