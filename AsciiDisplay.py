import random as rm

class disDot(object):
    def __init__(self, sym, x, y):
        self.sym = sym
        self.x = x
        self.y = y

def canWrite(dis, dot, xshift=0, yshift=0):
    if (0 <= (dot.y - yshift) < len(dis)) and (0 <= (dot.x - xshift) < len(dis[dot.y - yshift])):
        return True
    else: return False

def disDrawBox(dis, x, y, w, h, sym, xshift=0, yshift=0):
    for col in xrange(x, w):
        for cell in xrange(y, h):
            c = disDot(sym, col, cell)
            disWrite(dis, c, xshift, yshift)

def disDrawCircle(dis, x, y, r, sym, xshift=0, yshift=0):
    #print x, y
    for col in xrange(x-r-1, x+r+1):
        for cell in xrange(y-r-1, y+r+1):
            if (col-x)**2 + (cell-y)**2 <= r*r:
                #print col, cell
                c = disDot(sym, col, cell)
                disWrite(dis, c, xshift, yshift)

def disInit(dis, width, height):
    dis = []
    for row in xrange(height):
        dis.append([])
        for cel in xrange(width):
            dis[row].append(" ")
    return dis

def disHeader(text, width, sym="-"):
    header = "+" + str(text).center(width, sym) + "+\n"
    return header

def disRJust(text, width, rshift=0, sym=" "):
    return text.rjust(width - rshift + 3, sym)

def disPrint(dis, header="", footer=""):
    br = "|"
    print disHeader(header)
    for row in dis:
        print br + "".join(row) + br
    print disHeader(footer)

def disWrite(dis, dot, xshift=0, yshift=0):
    if (0 <= (dot.y - yshift) < len(dis)) and (0 <= (dot.x - xshift) < len(dis[dot.y - yshift])):
        dis[dot.y - yshift][dot.x - xshift] = dot.sym
