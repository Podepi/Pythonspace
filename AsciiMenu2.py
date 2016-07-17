# coding=utf-8
import curses, curses.panel
import random as rm
from AsciiDisplay import *
import rmplanet
from rmword import calcDist

class MenuStore(object):
    def __init__(self):
        self.winlist = []
        self.panellist = []

menu_store = MenuStore()

def drawMap(player, galaxy, y, x, h, w, view_y=0, view_x=0):
    win = curses.newwin(h,w, y,x)
    win.erase()
    
    yshift = view_y - int(h/2)
    xshift = view_x - int(w/2)
    selected = None
    current = "Deep Space"
    
    disDrawCircle(win, player.y - yshift, player.x - xshift, player.range, curses.ACS_CKBOARD, color=curses.color_pair(5))
    
    for p in galaxy.planets:
        try:
            if p.y == view_y and p.x == view_x:
                selected = p
            if p.y == player.y and p.x == player.x:
                current = p.name
            if (p.x-player.x)**2 + (p.y-player.y)**2 <= player.range*player.range:
                win.addch(p.y-yshift, p.x-xshift, p.sym, curses.color_pair(17))
            else:
                win.addch(p.y-yshift, p.x-xshift, p.sym, curses.color_pair(9))
        except:
            pass
    
    win.border(0, 0, 0, 0, 0, curses.ACS_TTEE, curses.ACS_LTEE, 0)
    win.addstr(0, int(w/2)-5, " {} ".format("Local Map"), curses.color_pair(16))
    win.addstr(1, 1, "Range: {}ly | Location: {} ".format(player.range, current), curses.color_pair(16))
    
    #draw pointer
    win.addch(h/2+2, w/2, "^", curses.color_pair(7))
    win.addch(h/2, w/2-2, ">", curses.color_pair(7))
    win.addch(h/2, w/2+2, "<", curses.color_pair(7))
    win.addch(h/2-2, w/2, "v", curses.color_pair(7))
    
    panel = curses.panel.new_panel(win)
    return win, panel, selected

def drawTrade(player, y,x, h,w, ptr=0):
    win = curses.newwin(h,w, y,x)
    win.erase()
    
    win.hline(3,1, curses.ACS_HLINE, w-2)
    win.vline(2,26, curses.ACS_VLINE, h-3)
    win.vline(2,34, curses.ACS_VLINE, h-3)
    win.vline(2,42, curses.ACS_VLINE, h-3)
    win.addstr(2,1, "Commodities")
    win.addstr(2,27, "Price")
    win.addstr(2,35, "Stock")
    win.addstr(2,43, "Cargo")
    
    line = 4
    
    for p in player.planet.comm:
        color = curses.color_pair(209)
        if line-4 == ptr:
            color = curses.color_pair(16)
        try:
            win.addstr(line, 1, player.planet.comname[line-4], color)    #name
            win.addstr(line, 27, str(p)+"c", color)                      #price
            win.addstr(line, 35, "inf", color)                           #stock
            win.addstr(line, 43, str(player.cargo[line-4])+"t", color)   #cargo
        except:
            pass
        line += 1
    
    win.border(0, 0, 0, 0, 0, curses.ACS_TTEE, curses.ACS_LTEE, curses.ACS_BTEE)
    win.addstr(0, int(w/2)-5, " {} ".format("Trading Screen"), curses.color_pair(16))
    win.addstr(1, 1, "Credits: {} | Hold: {}/{} ".format(player.credits, player.cargotot, player.cargomax), curses.color_pair(16))
    
    panel = curses.panel.new_panel(win)
    return win, panel

def makePanel(h,w, y,x, title, text):
    win = curses.newwin(h,w, y,x)
    win.erase()
    win.box()
    win.addstr(0, int(w/2) - int(len(title)/2), " {} ".format(title))
    
    disWritePara(win, 1, 1, h, w, text)
    
    panel = curses.panel.new_panel(win)
    return win, panel

def makeInfoPanel(h,w, y,x, title, info):
    win = curses.newwin(h,w, y,x)
    win.erase()
    
    if title == "<Planet>":
        title = "Target: {}".format(info.name.capitalize())
        ln = 1
        ln += disWritePara(win, ln, 1, h, w, "{:^29}".format(info.empr))
        ln += disWritePara(win, ln, 1, h, w, "Population:{:>18}".format(info.popl))
        ln += disWritePara(win, ln, 1, h, w, "Tech:{:>24}".format(info.tech + " Age"))
        ln += disWritePara(win, ln, 1, h, w, "Wealth rating:{:>15}".format(info.wealth), )
        ln += disWritePara(win, ln, 1, h, w, "Production:{:>18}".format(info.prod))
        ln += disWritePara(win, ln, 1, h, w, "Avg. Temp:{:>19}".format(str(info.temp) + "*C"))
        ln += disWritePara(win, ln, 1, h, w, "Distance:{:>20}".format(str(info.range) + "ly"))
        win.addstr(8, 1, "+---------------------------+")
        win.addstr(8, 9, " Useful Notes ", curses.color_pair(16))
        ln += 1
        for item in info.desc:
            ln += disWritePara(win, ln, 1, h, w-2, "> " + item)
            if ln >= w:
                break;
        
    #disWritePara(win, 1, 1, h, w, text)
    win.border(0, 0, 0, 0, curses.ACS_TTEE, 0, curses.ACS_BTEE, curses.ACS_RTEE)
    win.addstr(0, int(w/2) - int((len(title)+2)/2), " {} ".format(title), curses.color_pair(16))
    
    panel = curses.panel.new_panel(win)
    return win, panel

def menuMap(screen, player, galaxy, mvptr=(0, 0)):
    #print mvptr
    menu_store.panellist = []
    menu_store.winlist = []
    screen.erase()
    player.menu = "map"
    screen.box()
    win1, panel1, selected = drawMap(player, galaxy, 0,0,22,50, mvptr[0],mvptr[1])
    win2, panel2 = None, None
    if selected == None:
        selected = rmplanet.Planet()
    else:
        selected.range = calcDist(player.x, player.y, selected.x, selected.y, 1)
        win2, panel2 = makeInfoPanel(22,31, 0,49, "<Planet>", selected)
    #win2, panel2 = makePanel(10,10, 5,33, "test")
    menu_store.panellist.append(panel1)
    menu_store.winlist.append(win1)
    try:
        menu_store.panellist.append(panel2)
        menu_store.winlist.append(win2)
    except: pass
    #screen.vline(1, 33, "|", 22)
    
    screen.addstr(22, 1, " J:Jump | T:Trade".rjust(78), curses.color_pair(232))
    
    return win1, panel1, selected

def menuTrade(screen, player, ptr):
    planet = player.planet
    screen.erase()
    player.menu = "trade"
    screen.box()
    message = ""
    ptr[0] = ptr[0] % len(player.planet.comm)
    if ptr[1] == "max":
        max_buy = int(player.credits/player.planet.comm[ptr[0]])
        if  player.cargo[ptr[0]] > 0:
            player.credits += player.cargo[ptr[0]] * player.planet.comm[ptr[0]]
            player.cargotot -= player.cargo[ptr[0]]
            player.cargo[ptr[0]] = 0
            message = "Sold max"
        elif max_buy > 0:
            if max_buy > player.cargomax - player.cargotot:
                max_buy = player.cargomax - player.cargotot
            player.credits -= player.planet.comm[ptr[0]] * max_buy
            player.cargo[ptr[0]] += max_buy
            player.cargotot += max_buy
            message = "Bought max"
        else:
            message = "Not enough credits"
    elif ptr[1] > 0:
        if player.credits >= player.planet.comm[ptr[0]] and player.cargotot < player.cargomax:
            player.credits -= player.planet.comm[ptr[0]]
            player.cargo[ptr[0]] += ptr[1]
            player.cargotot += 1
        elif player.cargotot >= player.cargomax:
            message = "Not enough cargo space"
        else:
            message = "Not enough credits"
    elif ptr[1] < 0:
        if player.cargo[ptr[0]] > 0:
            player.credits += player.planet.comm[ptr[0]]
            player.cargo[ptr[0]] += ptr[1]
            player.cargotot -= 1
        else:
            message = "No cargo"
            
    win1, panel1 = drawTrade(player, 0,0, 22,50, ptr[0])
    win2, panel2 = makeInfoPanel(22,31, 0,49, "<Planet>", player.planet)
    
    screen.addstr(22, 1, "ARWS: Trade | Q: Trade max | M: Map ".rjust(78), curses.color_pair(232))
    screen.addstr(22, 1, message, curses.color_pair(10))
    return win1, panel1
