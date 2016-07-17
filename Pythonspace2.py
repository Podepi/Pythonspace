# coding=utf-8
import random as rm
import curses
from rmword import *
from rmplanet import *
from rmdesc2 import *
from AsciiDisplay import *
from AsciiMenu2 import *

class Galaxy(object):
    def __init__(self):
        self.visible = []
        self.size = 0
        self.planets = []
        self.pad = None
    def initPad(self):
        for p in self.planets:
            self.pad.addch(p.y, p.x, p.sym)

class Player(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cargo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cargotot = 0
        self.cargomax = 10
        self.credits = 100
        self.menu = "init"
        self.menuptr = [0, 0]
        self.planet = Planet()
        self.range = 5
        self.shipclass = ""
        self.shipdesc = ""
        self.shipname = ""
        self.shipsign = ""
        self.sym = "@"
        
    def jump(self, target):
        dist = calcDist(self.x, self.y, target.x, target.y, 1)
        if dist <= self.range:
            #self.range -= dist
            self.planet = target
            self.x = target.x
            self.y = target.y
            return dist
        else:
            mainscr.addstr(22, 1, "Out of range!", curses.color_pair(10))
            return False

'''stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
for i in range(0, curses.COLORS):
    for o in range(0, curses.COLORS):
        curses.init_pair(i, o, -1);'''
        
mainscr = curses.initscr()

panels = {"map":[]}

galaxy = Galaxy()
player = Player()
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

view_width = 79
view_height = 23

def genship():
    player.shipname = "{} {}".format(rm.choice(spfx), makeword(2))
    player.shipclass += "\n{} Class {}".format(makeword(2), rm.choice(sclas))
    player.shipsign += "{}-{}".format(makeword(1).upper(), rm.randint(0, 99999))
    player.shipdesc += "This ship has {} {} for its class.".format(rm.choice(squal), rm.choice(sstat))

def newGame():
    locations = []
    galaxy.size = 20
    #galaxy.pad = curses.newpad(galaxy.size, galaxy.size)
    #i = raw_input("Size of galaxy (default 20): ")
    #if i != '':
    #    galaxy.size = int(i)
        
    galaxy.num = 20
    #i = raw_input("Number of planets (default 20): ")
    #if i != '':
    #    galaxy.size = int(i)

    for i in xrange(galaxy.num):
        galaxy.planets.append(genNewPlanet())

        rx = rm.randint(0, galaxy.size - 1)
        ry = rm.randint(0, galaxy.size - 1)

        while locations.count( (rx, ry) ) != 1:
            galaxy.planets[i].x = rx
            galaxy.planets[i].y = ry
            locations.append( (rx, ry) )
            
    #galaxy.initPad()

    player.planet = galaxy.planets[rm.randint(0, len(galaxy.planets) - 1)]
    player.x = player.planet.x
    player.y = player.planet.y
    
    mainscr.addstr(0, 0, disHeader("Press 'M'", 80), curses.color_pair(3))
    disDrawCircle(mainscr, 12, 1, 5, ".")
    dim = mainscr.getmaxyx()
    disDrawBorder(mainscr, 0, 0, view_height, view_width, draw=[False, True, True, True])
    mainscr.refresh()
            
def main(stdscr):
    #curses.noecho()
    #curses.cbreak()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i+1, i, -1)
    curses.init_pair(17, 11, 18) # Yellow text, dark blue background
    curses.init_pair(16, -1, 19) # White text, dark blue background
    curses.init_pair(232, 14, 19) # Cyan text, dark blue background
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
    except curses.ERR:
        # End of screen reached
        pass
        
    win1 = "init"
    panel1 = "init"
    selected = ""
    stdscr.getch()
    
    newGame()
    
    while True:
        event = stdscr.getch()
#Initialise
        if event == ord("m"):
            player.menu = "map"
            player.menuptr = [player.y, player.x]
            win1, panel1, selected = menuMap(stdscr, player, galaxy, player.menuptr)
#Map screen
        if player.menu == "map":
            if event == ord("t"):
                player.menu = "trade"
                player.menuptr = [0, 0]
                win1, panel1 = menuTrade(stdscr, player, player.menuptr)
                
            elif event == ord("j"):
                dist = player.jump(selected)
                if dist != False:
                    player.menuptr = [player.y, player.x]
                    win1, panel1, selected = menuMap(stdscr, player, galaxy, player.menuptr)
                    mainscr.addstr(22, 1, "Consumed {}ly fuel".format(dist), curses.color_pair(10))
                    
            elif event == curses.KEY_LEFT:
                player.menuptr[1] -= 1
                win1, panel1, selected = menuMap(stdscr, player, galaxy, player.menuptr)
            elif event == curses.KEY_RIGHT:
                player.menuptr[1] += 1
                win1, panel1, selected = menuMap(stdscr, player, galaxy, player.menuptr)
            elif event == curses.KEY_UP:
                player.menuptr[0] -= 1
                win1, panel1, selected = menuMap(stdscr, player, galaxy, player.menuptr)
            elif event == curses.KEY_DOWN:
                player.menuptr[0] += 1
                win1, panel1, selected = menuMap(stdscr, player, galaxy, player.menuptr)
#Trading screen
        elif player.menu == "trade":
            if event == curses.KEY_ENTER:
                win1, panel1 = menuTrade(stdscr, player, [player.menuptr[0], "max"])
            elif event == curses.KEY_LEFT:
                player.menuptr[1] -= 1
                win1, panel1 = menuTrade(stdscr, player, player.menuptr)
            elif event == curses.KEY_RIGHT:
                player.menuptr[1] += 1
                win1, panel1 = menuTrade(stdscr, player, player.menuptr)
            elif event == curses.KEY_UP:
                player.menuptr[0] -= 1
                win1, panel1 = menuTrade(stdscr, player, player.menuptr)
            elif event == curses.KEY_DOWN:
                player.menuptr[0] += 1
                win1, panel1 = menuTrade(stdscr, player, player.menuptr)
            player.menuptr[1] = 0
        curses.panel.update_panels(); stdscr.refresh()
                

curses.wrapper(main)
