# coding=utf-8
import curses, curses.panel
from AsciiDisplay import *
import locale
import rmplanet

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
print code

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
    
    disDrawCircle(win, player.y - yshift, player.x - xshift, player.range, curses.ACS_BOARD, color=curses.color_pair(5))
    
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
    
    win.border(0, 0, 0, 0, 0, 0, curses.ACS_LTEE, 0)
    win.addstr(0, int(w/2)-5, " {} ".format("Local Map"), curses.color_pair(16))
    win.addstr(1, 1, "Range: {}ly | Location: {} ".format(player.range, current), curses.color_pair(16))
    
    #draw pointer
    win.addch(h/2+1, w/2, "^", curses.color_pair(7))
    win.addch(h/2, w/2-1, ">", curses.color_pair(7))
    win.addch(h/2, w/2+1, "<", curses.color_pair(7))
    win.addch(h/2-1, w/2, "v", curses.color_pair(7))
    
    panel = curses.panel.new_panel(win)
    return win, panel, selected

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
        title = " Target: {} ".format(info.name.capitalize())
        disWritePara(win, 1, 1, h, w, "{:^29}".format(info.empr))
        disWritePara(win, 2, 1, h, w, "Population:{:>18}".format(info.popl))
        disWritePara(win, 3, 1, h, w, "Tech level:{:>18}".format(info.tech))
        disWritePara(win, 4, 1, h, w, "Wealth rating:{:>15}".format(info.wealth))
        disWritePara(win, 5, 1, h, w, "Production:{:>18}".format(info.prod))
        disWritePara(win, 6, 1, h, w, "Avg. Temp:{:>19}".format(str(info.temp) + "*C"))
        disWritePara(win, 7, 1, h, w, disHeader("Useful Notes", 27))
        line = 8
        for item in info.desc:
            line += disWritePara(win, line, 1, h, w-2, "> " + item)
            if line >= w:
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
    win1, panel1, selected= drawMap(player, galaxy, 0,0, 23,50, mvptr[0],mvptr[1])
    win2, panel2 = None, None
    if selected == None:
        selected = rmplanet.Planet()
    else:
        win2, panel2 = makeInfoPanel(23,31, 0,49, "<Planet>", selected)
    #win2, panel2 = makePanel(10,10, 5,33, "test")
    menu_store.panellist.append(panel1)
    menu_store.winlist.append(win1)
    try:
        menu_store.panellist.append(panel2)
        menu_store.winlist.append(win2)
    except: pass
    #screen.vline(1, 33, "|", 22)
    return win1, panel1
