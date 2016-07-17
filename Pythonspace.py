import random as rm
from rmword import *
from rmplanet import *
from rmdesc2 import *
#import time

info = "Commands:\n - 'p' to enter hyperspace\n - 's' to change ship\n - 'o' to save most recent to file\n - Enter any other command for help"
most_recent = ""
spfx = ["The", "Starship", "Spaceship", "Starboat"]
sclas = ["Scout", "Transport", "Cargo Ship", "Starship",
    "Explorer", "Cruiser", "Frigate", "Destroyer", "Fighter",
    "Patroller", "Courier", "Starliner", "Miner", "Space Tug",
    "Shuttle", "Taxi", "Science Vessel", "Private Vessel",
    "Carrier", "Dreadnought", "Bomber", "Multipurpose Ship"]
sstat = ["handling", "engines", "weaponry", "shielding", "life support", "hyperdrive", "energy systems"]
squal = ["exceptional", "decent", "terrible", "appalling", "unreliable", "effective"]

def genship():
    s_desc = ""
    #s_desc += "- Your ship -".center(40)
    s_desc += "- {0} {1} -".format(rm.choice(spfx), makeword(2)).center(40)
    s_desc += "\n{0} Class {1}".format(makeword(2), rm.choice(sclas))
    s_desc += "\nCallsign: {0}-{1}".format(makeword(1).upper(), rm.randint(0, 99999))
    s_desc += "\nThis ship has {0} {1} for its class.".format(rm.choice(squal), rm.choice(sstat))
    return s_desc

#galaxy.size = int(raw_input("Type galaxy size (width):"))

print "\n" + genship()
print "\n" + info.center(40)

while True:
    inpt = raw_input().lower()
    if inpt == "p":
        most_recent = genplanet()
        print most_recent
    elif inpt == "s":
        most_recent = genship()
        print most_recent
    elif inpt == "o":
        out = "saved/" + str(len(most_recent)) + most_recent.strip(" -")[0:20].strip(" -")
        with open(out, "wr") as f:
            f.write(most_recent)
            print "Saved to: " + out
    else:
        print info
