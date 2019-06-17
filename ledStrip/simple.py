# https://dordnung.de/raspberrypi-ledstrip/ws2812

from rpi_ws281x import *

TOTAL_LED_COUNT = 300

# 18 = GPIO pin
# frequency:  800000  # LED signal frequency in hertz (usually 800khz)
# 5 = CMA CHANNEL
# 255 = LED BRIGHTNESS.

strip = Adafruit_NeoPixel(TOTAL_LED_COUNT, 18, 800000, 5, False, 255)
strip.begin()


LED_CHIP_NUMBER=10
R=255
G=255
B=255
strip.setPixelColorRGB(LED_CHIP_NUMBER, R, G, B)
strip.show()


