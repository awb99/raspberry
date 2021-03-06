import time
from rpi_ws281x import *

LED_COUNT = 300

LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

c=Color(200, 0, 0)

#for x in range(0, 300):
#    print("setting color for " + str(x))
#    strip.setPixelColor(x, c)
#    strip.show()

#colorWipe(strip,c)
#strip.show()
#time.sleep(1000)

try:
        while True:
            print ('red.')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            time.sleep(10)
            print ('green.')
            colorWipe(strip, Color(0, 255, 0))  # Geen wipe
            time.sleep(10)
            print ('blue.')
            colorWipe(strip, Color(0, 0, 255))  # Blue wipe
            time.sleep(10)
            print ('white.')
            colorWipe(strip, Color(255, 255, 255))  # white wipe
            time.sleep(10)


except KeyboardInterrupt:
    #if args.clear:
    colorWipe(strip, Color(0,0,0))

