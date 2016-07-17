import random as rm
from math import sqrt 

con = ("b", "c", "d", "g", "h",
    "k", "l", "m", "n", "p", "qu",
    "r", "s", "t", "v", "w", "x",
    "z", "ch", "th", "sh", "ph", "ng", "sc")

vow = ("a", "e", "i", "o", "u",
       "a", "e", "i", "o", "u", "y")

def calcDist(x1, y1, x2, y2, decround=-1):
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if decround > 0:
        dist *= (10 ** decround)
        dist = round(dist) / (10 ** decround)
    return dist

def genpop(min=0, max=-1):
    t = "{0} {1}".format(rmfile("adv_pop"), rmfile("adj_pop", line_min=min, line_max=max))
    #if rm.random() < 0.5:
    #    t += " with {0}".format(rmfile("noun_pop"))
    return t

def makeword(sylnum):
    word=""
    for i in xrange(sylnum):
        word = word + syl(rm.randint(2,3))
    word = word.capitalize()
    return word

def rmfile(target, line_num=-1, line_min=0, line_max=-1):
    out = ""
    with open("Desc/" + target) as f:
        val = list(f)
        if line_max < 0:
            line_max = len(val)-1
        if line_num < 0:
            line_num = rm.randint(line_min, line_max)
        out = val[line_num]
        
    if "/name/" in out:
        syl = out.split("/name/")
        out = out.replace("/name/".format(), makeword(2))

    if "/-pop/" in out:
        out = out.replace("/-pop/", genpop(0, 3))

    if "/pop/" in out:
        out = out.replace("/pop/", genpop())
    return out[0:len(out)-1]

def syl(letnum):
    s = ""
    vl = rm.randint(0, 1)
    for i in xrange(letnum):
        if vl == 0:
            s = s+rm.choice(con)
            vl = 1
        else:
            s = s+rm.choice(vow)
            vl = 0
    return s
    
