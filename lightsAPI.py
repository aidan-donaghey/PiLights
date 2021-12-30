import json
import time
# import lightsController as lc
import random
from rpi_ws281x import *
sP = "/rasplights/"

class lights():
  def __init__(self):
    # LED strip configuration:
    LED_COUNT      = 300      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
    #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    self.actions = {
        sP + "on": self.lightsOn,
        sP + "off": self.lightsOff,
        sP + "brightness": self.lightsBrightness,
        sP + "blue": self.lightsBlue,
        sP + "green": self.lightsRed,
        sP + "red": self.lightsGreen,
        sP + "setcolor": self.setcolor,

    }
    self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    self.strip.begin()
    self.brightness = 100
    self.color = (255,255,255)
  
  # On and Off States
  def lightsOn(self,*argv):
    print("Lights On")

  def lightsOff(self,*argv):
    print("Lights Off")

  def lightsBrightness(self,value:int,*argv):
    """Changes the lights brightness

    Args:
        value (int): int between 0 and 100 to change the brightness
    """
    print(f"Lights changed to {int(value)}% brightness")
  # Primary Colours
  def setcolor(self,*argv):
    x = json.loads(argv[0].payload.decode())
    color = [x["color"]["r"],x["color"]["g"],x["color"]["b"]]
    self.color = color
    print(f"Lights changed color to {*color,}")
    self.__solidColor(color)

  def __solidColor(self,color):
  # Converts the color from the json to the rpi_ws281x color
    finalcolor = Color(*color)
    t1 = time.time()
    for i in range(self.strip.numPixels()):
        self.strip.setPixelColor(i, finalcolor)
    t2 = time.time()
    print(t2-t1)
    self.strip.show()


 
  def lightsRed(self,*argv):
    print("Lights Red")
    finalcolor = Color(255,0,0)
    self.__solidColor(finalcolor)

  def lightsGreen(self,*argv):
    print("Lights Green")
    finalcolor = Color(0,255,0)
    self.__solidColor(finalcolor)

  def lightsBlue(self,*argv):
    print("Lights Blue")
    finalcolor = Color(0,0,255)
    self.__solidColor(finalcolor)


 