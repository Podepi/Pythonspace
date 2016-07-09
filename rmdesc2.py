from random import *
from rmword import *

def remove_end(word, suffix):
    while word.endswith(suffix):
        word = word[0:len(word)-1]
    return word

def gendesc(planet_name):
    d = ""
    counter = 0
    points = 0
    while counter < 3:
        if random() < 0.5 and counter == 0:
            d += "{1} {2} {3}".format(planet_name, rmfile("desc_env"), rmfile("adj_env"), rmfile("noun_env"))
            points += 1

        if random() < 0.5 and counter == 0:
            if points > 0:
                d += ", "
            d += "{1} {0}ian {2} {3}".format(remove_end(planet_name, vow), rmfile("desc_life"), rmfile("adj_life"), rmfile("noun_life"))
            points += 1

        if random() < 0.5 and counter == 1:
            if points > 0:
                d += ", "
            d += genpop()
            d += " for its {0} {1}".format(rmfile("adj_art"), rmfile("noun_art"))
            points += 1

        if random() < 0.5 and counter == 2:
            if points > 0:
                d += ", "
            d += "{0} {1} {2}".format(rmfile("desc_plague"), rmfile("adj_plague"), rmfile("noun_plague"))
            points += 1

        counter += 1
    if points == 0:
        d += "a tedious place"
    d += "."
    return d[0].upper() + d[1:len(d)]
