import curses
from AsciiDisplay import *
from rmword import calcDist

info = "Commands:\n - 'm' to show map\n - 'p' to enter hyperspace\n - 's' to change ship\n - 'o' to save most recent to file\nEnter any other command for help"

def menuPlanet(p, width):
    line = ""
    output = disHeader(p.name, screen, " ")
    line = "|Allegiance: {}".format(p.empr)
    output += line + disRJust("|\n", width, len(line))

    line = "|Population: {}".format(p.popl)
    output += line + disRJust("|\n", width, len(line))

    line = "|Tech level: {} Age".format(p.tech)
    output += line + disRJust("|\n", width, len(line))

    line = "|Wealth:     {}".format(p.wealth)
    output += line + disRJust("|\n", width, len(line))

    line = "|Production: {}".format(p.prod)
    output += line + disRJust("|\n", width, len(line))

    line = u"|Avg. Temp:  {}*C".format(p.temp).encode("utf-8")
    output += line + disRJust("|\n", width, len(line))

    output += disHeader("Useful Notes",  screen)
    
    if len(p.desc) > 0:
        for note in p.desc:
            line = "- " + note[0].upper() + note[1:len(note)]
            output += line + disRJust("|\n", width, len(line))
    else: output += "- This planet is a tedious place"

    print output
    
    cmd = commandList([("t", "trade", "Trade goods", p), ("m", "map", "To map view")])


def menuShip(s, width):
    line = ""
    disHeader(s.shipname, screen)
    
    line += s.shipclass

def drawList(y, x, screen, items):
    for i in xrange(len(items)):
        screen.addstr(x, y+i, items[i])
    screen.refresh()

def drawMap(screen, player, galaxy):
    dim = screen.getmaxyx()
    screen.clear()
    
    mapheight = 20
    mapwidth = 32
    
    x = player.x - int(mapwidth/2) - 1
    y = player.y - int(mapheight/2) - 1
    #draw = []
    #draw = disInit(draw, view_width, view_height)
    #output = ""
    galaxy.visible = []
    in_range = []
    out_range = []
    
    #disDrawBorder(screen, 0, 0, dim[1] - 1, dim[0] - 1)

    screen.addstr(0, 0, disHeader("Local Map", screen))
    disDrawCircle(screen, mapheight - 1, player.x - x, player.range, ".")

    #disWrite(draw, player, x, y)
    loop = 0
    galaxy.pad.refresh(y,x, 1,1, mapheight, mapwidth)
    
    #screen.addstr(mapheight+2, 0, disHeader("Systems in range:", stdscr))

    '''for p in in_range:
        loop += 1
        line = "|" + str(loop) + " - " + p.name
        if p.range == 0:
            range = ("Current location|").rjust(dim[1]+2-len(line), " ")
        else:
            range = (str(p.range)+"ly|").rjust(dim[1]+2-len(line), " ")
        if loop + mapheight + 2 < dim[0]:
            screen.addstr(mapheight+2+loop, 0, line + range)
        
    loop += 1
    screen.addstr(mapheight+2+loop, 0, disHeader("Out of range:", stdscr))

    for p in out_range:
        loop += 1
        line = "|" + str(loop) + " - " + p.name
        range = (str(p.range)+"ly|").rjust(dim[1]+2-len(line), " ")
        screen.addstr(mapheight+2+loop, 0, line + range)
        
    
    screen.refresh(0,0, 0,0, dim[0]-1,dim[1]-1)'''

    '''output += disHeader("", screen)
    print output
    inpt = raw_input("Type planet number for info, or b to go back: ")
    while "" != inpt != "b":
        inpt = int(inpt) - 1
        if inpt < len(in_range):
            menuPlanet(in_range[inpt], view_width)
        elif inpt < len(in_range) + len(out_range):
            menuPlanet(out_range[inpt - len(in_range)], view_width)
        else:
            print "Out of range"
        inpt = raw_input("Type planet number for info, or b to go back: ")
        
    if inpt == "b" or inpt == "":
        print "\n" + info'''
