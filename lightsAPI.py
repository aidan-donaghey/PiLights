sP = "/rasplights/"

def lightsOn():
  print("Lights On")

def lightsOff():
  print("Lights Off")

def lightsBlue():
  print("Lights Blue")

def lightsRed():
  print("Lights Red")


def lightsGreen():
  print("Lights Red")


actions = {
    sP + "on": lightsOn,
    sP + "off": lightsOff,
    sP + "blue": lightsBlue,
    sP + "green": lightsRed,
    sP + "red": lightsGreen,
}