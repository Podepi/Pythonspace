from random import *
from rmword import *

def remove_end(word, suffix):
    while word.endswith(suffix):
        word = word[0:len(word)-1]
    return word

def gendesc(planet_name):
    d = []
    if random() < 0.5:
        d.append("{} {} {}".format(rmfile("desc_env").capitalize(), rmfile("adj_env"), rmfile("noun_env")))

    if random() < 0.5:
        d.append("{} {}ian {} {}".format(rmfile("desc_life").capitalize(), remove_end(planet_name, vow), rmfile("adj_life"), rmfile("noun_life")))

    if random() < 0.5:
        d.append(genpop().capitalize() + " for its {} {}".format(rmfile("adj_art"), rmfile("noun_art")))

    if random() < 0.5:
        d.append("{} {} {}".format(rmfile("desc_plague").capitalize(), rmfile("adj_plague"), rmfile("noun_plague")))
    if len(d) == 0:
        d.append("This planet is a tedious place")
    return d
