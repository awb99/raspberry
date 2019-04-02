# https://dordnung.de/raspberrypi-ledstrip/ws2812

# power: 
# 1 LED up to 60mA
# 1 meter = 60 LED: 3600 mA = 3.6A
# 5 meter @ 60 leds/meter = 300 leds = 18A

# Netzteil 50W 5V 10A  => Das Netzteil kann 2.5 meter betreiben.
# power supply ground needs to be connected to ground of converter, and ground of raspberry

#  It is important that GND / ground is connected to both the Raspberry Pi and the external power supply. 

# 6 x TXS0108E Logic Level Converter
# converts Raspberry 3.3V to 5V

# the power supply

# For the LED-Strip only the GPIO18 pin and one of the ground pins of the Raspberry Pi are required.
# GPIO18 = port 12. PCM CLK (6th from the top, right)

# Since WS281X LED-Strips require a high clock accuracy, the audio kernel module must be deactivated on newer Raspberry Pis. 

# Unless you're using SPI, rpi_ws281x requires root in order to access hardware registers it needs to generate the ws281x protocol on the Pi.

# Depending on the length of the LED strip, the external power connection should be installed in several places. 
# Ideally, the VCC and GND will be connected in parallel with the switching power supply on approximately every meter
#  (so that many cables will lead to the power supply input).



# The brightness of the WS2801 is higher.
# It is also possible to control the WS2801 and play music, which is not possible with the WS2812 (more on this below)
# WS2801B strips have two data lines (data and clock), whereby individual LEDs can be addressed via the 
# integrated SPI bus of the Raspberry Pi.

# This is different for the WS2812B models. These strips have only a single data pin, which is why before sending a
# lot more has to be calculated. For this reason the WS2801B RGB LED strips are preferable to the WS2812 for use 
# on the Raspberry Pi, despite their supposedly smaller “serial number”.

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


