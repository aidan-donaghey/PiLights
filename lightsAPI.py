import json
sP = "/rasplights/"

class lights():
  def __init__(self):
    self.actions = {
        sP + "on": self.lightsOn,
        sP + "off": self.lightsOff,
        sP + "brightness": self.lightsBrightness,
        sP + "blue": self.lightsBlue,
        sP + "green": self.lightsRed,
        sP + "red": self.lightsGreen,
        sP + "setcolor": self.setcolor,

    }
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
    # print(argv[0].payload.decode())
    x = json.loads(argv[0].payload.decode())
    print(x.color)
    # print(f"Lights changed color to {argv[0]},{argv[1]},{argv[2]}")


  def lightsBlue(self,*argv):
    print("Lights Blue")

  def lightsRed(self,*argv):
    print("Lights Red")

  def lightsGreen(self,*argv):
    print("Lights Green")


 