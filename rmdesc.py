from random import *

def gendesc(planet_name):
    adv_pop = ["extremely", "widely", "somewhat", "mildly", "only slightly"]
    adj_pop = ["hated", "infamous", "unpopular", "controversial", "noted", "famous", "known", "popular", "famous"]
    noun_pop = ["tourists", "traders", "pirates", "miners", "visitors", "travellers", "freelancers", "pilots", "neighbouring planets"]

    desc_env = ["covered in", "mostly covered in", "famous for its", "slowly losing its"]
    adj_env = ["vast", "colourful", "diverse", "thick", "vibrant", "weird", "toxic", "seemingly endless",
        "meandering", "dry", "rainy", "coastal", "tropical", "polar", "calm", "stormy", "cloudy", "arctic",
        "arid", "humid", "reflective", "green", "blue", "yellow", "pink", "red", "wavy"]
    noun_env = ["rainforests", "forests", "grasslands", "deserts", "oceans", "deep oceans", "seas", "tundra", "rivers", "shrublands"]

    desc_life = ["{0} {1} for".format(choice(adv_pop), choice(adj_pop)), "home to", "infested with", "teeming with"]
    adj_life = ["tree", "cactus", "grass", "leaf", "fire", "ice", "water", "shimmering", "aggressive", "tame"
        "poisonous", "venomous", "colourful", "camoflaged", "endangered", "plentiful", "tasty", "toxic",
        "harmless", "docile", "brave", "timid", "intelligent", "dumb", "giant", "tiny", "weird", "vibrant",
        "speedy", "slow", "depressed", "mountain", "valley", "river", "snow", "jumping", "vicious", "crested",
        "shelled", "psychic", "edible", "tall", "short", "angry", "emotionless", "leathery", "flightless", "flying",
        "floating", "strong", "deaf", "blind", "oblong", "rectangular", "white", "grey", "brown", "black", "albino",
        "ravenous", "mud"]
    noun_life = ["worm", "grub", "wolf", "scorpion", "plant", "fruit", "root", "fish", "bird", "monkey", "ant", "whale",
        "sloth", "snake", "urchin", "ape", "rat", "mouse", "tree", "vine", "bug", "goat", "shrew", "coral", "lichen",
        "shrub", "insect", "spider", "seed", "squid", "dolphin", "seed", "octopus", "lizard", "mosquito", "beetle",
        "chicken", "jellyfish", "monster", "bugblatter beast", "dragon", "crab", "fox", "squirrel", "starfish"]

    adj_art = ["foreboding", "weird", "simple", "elegant", "futuristic", "impressive", "towering", "complicated",
        "neat and tidy", "complex", "old-fashioned", "antequated", "high-tech", "clean", "dirty", "hoopy", "efficient",
        "inefficient", "monolithic", "jagged", "chaotic", "orderly", "dark", "bright", "light", "heavy", "brooding",
        "expensive", "cheap", "cyclopean", "oblong", "messy", "blocky", "abstract", "ambient", "classic"]
    noun_art = ["architecture", "buildings", "cities", "casinos", "music", "art", "hotels", "movies", "public transport"]

    adj_food = ["sweet", "tasty", "vicious", "bitter", "salted"]
    noun_food = ["soup", "gargle blasters", "brew", "food pills", "stew", "nut", "fruit", "water"]

    adj_plague = ["infrequent", "deadly", "frequent", "lethal", "rampant", "occasional"]
    noun_plague = ["heavy traffic", "disease", "civil war", "organised crime", "poverty", "tidal waves"
            "global storms", "earthquakes", "meteor storms", "solar flares", "industrial accidents"]
    
    d = planet_name
    counter = 0
    while counter < 3:
        if random() < 0.5 and counter == 0:
            d += " {1} {2} {3}, ".format(planet_name, choice(desc_env), choice(adj_env), choice(noun_env))
            d += "{1} the {0}ian {2} {3}".format(planet_name, choice(desc_life), choice(adj_life), choice(noun_life))
            counter += 2

        if random() < 0.5 and counter == 1:
            d += " is {0} {1} ".format(choice(adv_pop), choice(adj_pop))
            if random() < 0.5:
                d += "among {0} ".format(choice(noun_pop))
            d += "for its {0} {1}".format(choice(adj_art), choice(noun_art))

        if random() < 0.5 and counter == 2:
            if d != planet_name:
                d += ", but"
            d += " is plagued by {0} {1}".format(choice(adj_plague), choice(noun_plague))

        counter += 1
    if d == planet_name:
        d += " is a tedious place"
    d += "."
    return d 
