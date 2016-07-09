import random as rm

con = ("b", "c", "d", "th", "g", "h",
    "k", "l", "m", "n", "p", "ch",
    "qu", "r", "s", "t", "v", "w",
    "x", "z", "sh", "ph", "ng")

vow = ("a", "e", "i", "o", "u",
       "a", "e", "i", "o", "u", "y")

def genpop(min=0, max=-1):
    t = "{0} {1}".format(rmfile("adv_pop"), rmfile("adj_pop", line_min=min, line_max=max))
    if rm.random() < 0.5:
        t += " among {0}".format(rmfile("noun_pop"))
    return t

def makeword(sylnum):
    word=""
    for i in xrange(sylnum):
        word = word + syl(rm.randint(2,3))
    word = word.capitalize()
    return word

def rmfile(target, line_num=-1, line_min=0, line_max=-1):
    out = ""
    with open(target) as f:
        val = list(f)
        if line_max < 0:
            line_max = len(val)-1
        if line_num < 0:
            line_num = rm.randint(line_min, line_max)
        out = val[line_num]

    if "/-pop/" in val[line_num]:
        gp = genpop(0, 3)
        out = out.replace("/-pop/", gp)

    if "/pop/" in val[line_num]:
        gp = genpop()
        out = out.replace("/pop/", gp)
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