import random as rm
import curses

def canWrite(screen, y, x):
    if (0 <= y < screen.getmaxyx()[0]) and (0 <= x < screen.getmaxyx()[1]):
        return True
    else: return False
'''def initColor(col):
    curses.init_color(1, )'''
    
def disDrawBorder(screen, top, left, bot, right, sym=("=", "|", "+"), draw=(True, True, True, True)):
    #sym = (horizontal, vertical, corner)
    #draw = top, left, bottom, right
    for x in xrange(left, right):
        if draw[0]:
            if canWrite(screen, top, x):
                screen.addch(top, x, sym[0])
        if draw[2]:
            if canWrite(screen, bot, x):
                screen.addch(bot, x, sym[0])
                
    for y in xrange(top, bot):
        if draw[1]:
            if canWrite(screen, y, left):
                screen.addch(y, left, sym[1])
        if draw[3]:
            if canWrite(screen, bot, right):
                screen.addch(y, right, sym[1])
    try: screen.addch(top, left, sym[2])
    except: pass
    try: screen.addch(top, right, sym[2])
    except: pass
    try: screen.addch(bot, left, sym[2])
    except: pass
    try: screen.addch(bot, right, sym[2])
    except: pass

def disDrawBox(screen, y, x, h, w, sym):
    for col in xrange(x, x + w):
        for cell in xrange(y, y + h):
            try:
                screen.addch(cell, col, sym)
            except: pass

def disDrawCircle(screen, y, x, r, sym, xshift=0, yshift=0, color=None):
    #print x, y
    if color == None:
        color=curses.color_pair(0)
    for col in xrange(x-r, x+r+1):
        for cell in xrange(y-r, y+r+1):
            if (col-x)**2 + (cell-y)**2 <= r*r:
                try:
                    screen.addch(cell - yshift, col - xshift, sym, color)
                except: pass
    #screen.refresh()

def disHeader(text, screen, sym="-"):
    header = "+" + str(text).center(screen.getmaxyx()[1]-2, sym) + "+"
    return header

def disRJust(text, screen, rshift=0, sym=" "):
    return text.rjust(screen.getmaxyx()[1] - rshift + 3, sym)

def disPrint(dis, header="", footer=""):
    br = "|"
    print disHeader(header)
    for row in dis:
        print br + "".join(row) + br
    print disHeader(footer)

def disWrite(screen, dot, xshift=0, yshift=0):
    #if (0 <= (dot.y - yshift) < len(dis)) and (0 <= (dot.x - xshift) < len(dis[dot.y - yshift])):
    
    screen.addch(dot.y - yshift, dot.x - xshift, dot.sym)
    
def disWritePara(screen, y, x, h, w, text):
    words = text.split(" ")
    line = 0
    output = [""]
    for word in words:
        if len(word) > w:
            word = word[0:w]
        if len(word) + len(output[line]) > w or word.startswith("\n"):
            output.append("")
            line += 1
            if line >= h:
                break

        word += " "
        output[line] += word.replace("\n", "")
    line = 0
    for l in output:
        screen.addstr(line+y, x, l)
        line += 1
