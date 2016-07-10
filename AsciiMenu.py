from AsciiDisplay import *
from rmword import calcDist

info = "Commands:\n - 'm' to show map\n - 'p' to enter hyperspace\n - 's' to change ship\n - 'o' to save most recent to file\nEnter any other command for help"

def menuPlanet(p, width):
    line = ""
    output = disHeader("( " + p.name + " )", width)
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

    line = "|Avg. Temp:  {}*C".format(p.temp)
    output += line + disRJust("|\n", width, len(line))

    output += disHeader("Useful Notes",  width)
    
    if len(p.desc) > 0:
        for note in p.desc:
            line = "- " + note[0].upper() + note[1:len(note)]
            output += line + disRJust("|\n", width, len(line))
    else: output += "- This planet is a tedious place"

    output += disHeader("", width)
    print output

def drawMap(player, galaxy, view_width, view_height):
    x = player.x - (view_width/2)
    y = player.y - (view_height/2)
    draw = []
    draw = disInit(draw, view_width, view_height)

    output = disHeader("Local Map", view_width)
    galaxy.visible = []
    in_range = []
    out_range = []

    disDrawCircle(draw, player.x, player.y, player.range, ".", x, y)

    for p in galaxy.planets:

        disWrite(draw, p, x, y)

        if canWrite(draw, p, x, y) == True:
            p.range = calcDist(p.x, p.y, player.x, player.y, 1)
            if p.range <= player.range:
                in_range.append(p)
            else:
                out_range.append(p)
            galaxy.visible.append(p)

    #disWrite(draw, player, x, y)

    for row in xrange(view_height):
        output += "|"
        for cell in xrange(view_width):
            output += draw[row][cell]
        output += "|\n"

    loop = 0

    output += disHeader("Systems in range:", view_width)

    for p in in_range:
        loop += 1
        line = "|" + str(loop) + " - " + p.name
        if p.range == 0:
            range = ("Current location|").rjust(view_width+2-len(line), " ")
        else:
            range = (str(p.range)+"ly|").rjust(view_width+2-len(line), " ")
        output += line + range + "\n"

    output += disHeader("Out of range:", view_width)

    for p in out_range:
        loop += 1
        line = "|" + str(loop) + " - " + p.name
        range = (str(p.range)+"ly|").rjust(view_width+2-len(line), " ")
        output += line + range + "\n"

    output += disHeader("", view_width)
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
        print "\n" + info
