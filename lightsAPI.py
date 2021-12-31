import json
import time
from multiprocessing import Process
# import lightsController as lc
import random
from rpi_ws281x import *
from strandtest import rainbow
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
    """This contains all of the actions that can be called after rasplights"""
    self.actions = {
        sP + "on": self.lightsOn,
        sP + "off": self.lightsOff,
        sP + "brightness": self.lightsBrightness,
        sP + "blue": self.lightsBlue,
        sP + "green": self.lightsGreen,
        sP + "red": self.lightsRed,
        sP + "setcolor": self.setcolor,
        sP + "rainbow": self.rainbowOn,


    }
    self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    self.strip.begin()
    self.brightness = 1
    self.color = [255,255,255]
    self.rainbow = False
    self.rainbowprocess = Process(target=self.rainbowFunction, args=(1,))
  
  # On and Off States
  def lightsOn(self,*argv):
    self.brightness = 1
    self.color = [255,255,255]
    self.__solidColor()
    print("Lights On")
  

  def lightsOff(self,*argv):
    self.brightness = 0
    self.__solidColor()

  def lightsBrightness(self,value:int,*argv):
    """Changes the lights brightness

    Args:
        value (int): int between 0 and 100 to change the brightness
    """
    self.brightness = (float(value.payload.decode())/100.0)
    print(f"Lights changed to {self.brightness}% brightness")
    self.__solidColor()
  


  def setcolor(self,*argv):
    """This takes in a color within a JSON file formatted as "color": {
    "r": 255,
    "g": 0,
    "b": 155 }
    """
    x = json.loads(argv[0].payload.decode())
    color = [x["color"]["r"],x["color"]["g"],x["color"]["b"]]
    self.color = color
    print(f"Lights changed color to {*color,}")
    self.__solidColor()

  def __solidColor(self):
    """This is the function that actually sets the color of the LED's for a solid color. It is called for all brightness' and colors.
    """
    if self.rainbow == True:
      self.rainbow = False
      self.rainbowToggle()
  # Converts the color from the json to the rpi_ws281x color
    t1 = time.time()
    newarray =[]
    for x in self.color:
      print(f"Colour: {x}")
      print(f"Adapted values: {int(x * self.brightness)}")
      newarray.append(int(x * self.brightness))

    finalcolor = Color(*newarray)
    
    for i in range(self.strip.numPixels()):
        self.strip.setPixelColor(i, finalcolor)
    t2 = time.time()
    print(t2-t1)
    self.strip.show()


  def lightsRed(self,*argv):
    """Wrapper for setting red solid color.
    """
    print("Lights Red")
    finalcolor = [255,0,0]
    self.color = finalcolor
    self.__solidColor()

  def lightsGreen(self,*argv):
    """Wrapper for setting green solid color.
    """
    print("Lights Green")
    finalcolor = [0,255,0]
    self.color = finalcolor
    self.__solidColor()

  def lightsBlue(self,*argv):
    """Wrapper for setting blue solid color.
    """
    print("Lights Blue")
    finalcolor = [0,0,255]
    self.color = finalcolor
    self.__solidColor()


  def rainbowOn(self,*argv):
    """It turns on the rainbow Effect. It sets self.rainbow to True and runs rainbowToggle()
    """
    if self.rainbow == False:
      self.rainbow = True
      self.rainbowToggle()
  
  def rainbowToggle(self,*argv):
    """Starts or stops the rainbow process.
    """
    if self.rainbow == True:
      self.rainbowprocess.start()
    elif self.rainbow == False:
      self.rainbowprocess.terminate()
      print("The rainbow Process is terminated")
      self.rainbowprocess.join()
      print("The rainbow Process is joined")
      
  
    

  def wheel(self,pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

  def rainbowFunction(self,wait_ms = 1):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    while self.rainbow == True:
      for j in range(256):
          for i in range(self.strip.numPixels()):
              self.strip.setPixelColor(i, self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
          self.strip.show()
          time.sleep(wait_ms/1000.0)
 
  def clearAnimation(self):
    pass