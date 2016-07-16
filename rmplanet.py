import random as rm
from rmword import *
from rmdesc2 import *

pwealth = ["Impoverished", "Poor", "Average", "Rich", "Extremely rich"]
ptype = ["Agricultural", "Industrial", "Mining", "Mixed", "Scientific", "Cultural", "Military"]
ppop = ["000", "Million", "Billion"]
pera = ["Early", "Middle", "Late"]
ptech = ["Medieval", "Steam", "Industrial", "Atomic", "Space", "Information", "Robotic", "Cyberpunk", "Nanotech"]

class Planet(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.range = 0
        self.name = "None"
        self.fctn = "None"
        self.popl = "None"
        self.sym = "?"
        self.tech = "None"
        self.prod = "None"
        self.temp = 0
        self.desc = "None"

def genplanet():
    name = makeword(rm.randint(2,3))
    p_desc = ""
    p_desc += "- {0} -".format(name).center(40)
    p_desc += "\nOwnership:  {0} {1}".format(makeword(2) + " " + rm.choice(pempr))
    p_desc += "\nPopulation: {0} {1}".format(rm.randint(1, 999), rm.choice(ppop))
    p_desc += "\nTech level: {0} {1} Age".format(rm.choice(pera), rm.choice(ptech))
    p_desc += "\nProduction: {0} {1}".format(rm.choice(pwealth), rm.choice(ptype))
    p_desc += "\nAvg. Temp:  {0}*C".format(rm.randint(-200, 200))
    #p_desc += "\nThis planet {0}".format(rm.choice(pdesc))
    p_desc += "\n" + gendesc(name)
    return p_desc

def genNewPlanet():
    planet = Planet()
    planet.name = makeword(rm.randint(2,3))
    planet.empr = rmfile("planet/empire")
    planet.popl = str(rm.randint(1, 999)) + " " + rm.choice(ppop)
    planet.tech = rm.choice(pera) + " " + rm.choice(ptech)
    planet.wealth = rm.choice(pwealth)
    planet.prod = rm.choice(ptype)
    planet.temp = rm.randint(-200, 200)
    planet.desc = gendesc(planet.name)
    planet.sym  = planet.name[0]
    return planet
