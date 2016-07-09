import random as rm
from rmword import *
from rmdesc2 import *

pval = ["Poor", "Average", "Mainly", "Rich"]
ptype = ["Agricultural", "Industrial", "Mining"]
pempr = ["Republic", "Co-operative", "Empire", "Federation", "Union", "Corporation", "Feudal States",
        "Leadership", "Foundation", "Organisation", "Coalition", "Agency", "States", "Monarchy", "Collective",
        "House", "Party", "Conglomerate", "Society", "Industries", "Nations", "Dictatorship", "Democracy",
        "Theocracy", "Division", "Cult", "Sector", "Laboratories"]
ppop = ["000", "Million", "Billion"]
pera = ["Early", "Middle", "Late"]
ptech = ["Medieval", "Steam", "Industrial", "Atomic", "Space", "Information", "Robotic", "Cyberpunk", "Nanotech"]

def genplanet():
    name = makeword(rm.randint(2,3))
    p_desc = ""
    p_desc += "- {0} -".format(name).center(40)
    p_desc += "\nOwnership:  {0} {1}".format(makeword(2), rm.choice(pempr))
    p_desc += "\nPopulation: {0} {1}".format(rm.randint(1, 999), rm.choice(ppop))
    p_desc += "\nTech level: {0} {1} Age".format(rm.choice(pera), rm.choice(ptech))
    p_desc += "\nProduction: {0} {1}".format(rm.choice(pval), rm.choice(ptype))
    p_desc += "\nAvg. Temp:  {0}*C".format(rm.randint(-200, 200))
    #p_desc += "\nThis planet {0}".format(rm.choice(pdesc))
    p_desc += "\n" + gendesc(name)
    return p_desc