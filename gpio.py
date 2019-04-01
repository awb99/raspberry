import RPi.GPIO as GPIO
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

print(GPIO.RPI_INFO)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

cLED=40
cMotion=26

GPIO.setup(cLED, GPIO.OUT)
GPIO.setup(cMotion, GPIO.IN)

# GPIO.output(cLED, True)
# time.sleep(2)
# GPIO.output(cLED, False)
# time.sleep(5)

while True:
    if GPIO.input(cMotion):
        print("Motion Detected...")
        GPIO.output(cLED, True)
        time.sleep(1) #Buzzer turns on for 0.5 sec
        GPIO.output(cLED, False)
        time.sleep(2)
    time.sleep(0.1) #loop delay, should be less than detection delay


GPIO.cleanup()

