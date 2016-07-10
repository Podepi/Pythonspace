import random as rm
from rmword import *
from rmplanet import *
from rmdesc2 import *
from AsciiDisplay import *
from AsciiMenu import *
#import time

class Galaxy(object):
    def __init__(self):
        self.visible = []
        self.size = 0
        self.planets = []

class Player(disDot):
    def __init__(self):
        self.range = 5
        self.pln = Planet()
        self.sym = "@"

galaxy = Galaxy()
player = Player()
menu = "intro"
info = "Commands:\n - 'm' to show map\n - 'p' to enter hyperspace\n - 's' to change ship\n - 'o' to save most recent to file\nEnter any other command for help"
most_recent = ""
spfx = ["The", "Starship", "Spaceship", "Starboat"]
sclas = ["Scout", "Transport", "Cargo Ship", "Starship",
    "Explorer", "Cruiser", "Frigate", "Destroyer", "Fighter",
    "Patroller", "Courier", "Starliner", "Miner", "Space Tug",
    "Shuttle", "Taxi", "Science Vessel", "Private Vessel",
    "Carrier", "Dreadnought", "Bomber", "Multipurpose Ship"]
sstat = ["handling", "engines", "weaponry", "shielding", "life support", "hyperdrive", "energy systems"]
squal = ["exceptional", "decent", "terrible", "appalling", "unreliable", "effective"]

view_width = 40
view_height = 20
    
def genship():
    s_desc = ""
    #s_desc += "- Your ship -".center(40)
    s_desc += "- {} {} -".format(rm.choice(spfx), makeword(2)).center(40)
    s_desc += "\n{} Class {}".format(makeword(2), rm.choice(sclas))
    s_desc += "\nCallsign: {}-{}".format(makeword(1).upper(), rm.randint(0, 99999))
    s_desc += "\nThis ship has {} {} for its class.".format(rm.choice(squal), rm.choice(sstat))
    return s_desc

def newGame():
    locations = []
    galaxy.size = 20
    i = raw_input("Size of galaxy (default 20): ")
    if i != '':
        galaxy.size = int(i)
        
    galaxy.num = 20
    i = raw_input("Number of planets (default 20): ")
    if i != '':
        galaxy.size = int(i)

    for i in xrange(galaxy.num):
        galaxy.planets.append(genNewPlanet())

        rx = rm.randint(0, galaxy.size)
        ry = rm.randint(0, galaxy.size)

        while locations.count( (rx, ry) ) != 1:
            galaxy.planets[i].x = rx
            galaxy.planets[i].y = ry
            locations.append( (rx, ry) )

    player.pln = rm.randint(0, len(galaxy.planets) - 1)
    player.x = galaxy.planets[player.pln].x
    player.y = galaxy.planets[player.pln].y
            
newGame()

print "\n" + genship()
print "\n" + info.center(40)

while True:
    inpt = raw_input().lower()
    a = 0
    if inpt == "p":
        most_recent = genplanet()
        print most_recent
        menu = "planetOld"
    elif inpt == "s":
        most_recent = genship()
        print most_recent
        menu = "shipOld"
    elif inpt == "o":
        out = "saved/" + str(len(most_recent)) + most_recent.strip(" -")[0:20].strip(" -")
        with open(out, "wr") as f:
            f.write(most_recent)
            print "Saved to: " + out
    elif inpt == "m":
        drawMap(player, galaxy, view_width, view_height)
        menu = "map"
    else:
        print info
