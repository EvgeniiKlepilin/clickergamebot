"""

Bot for palying "Holiday City: Reloaded" on Steam.

Author: Evgenii Klepilin

The game must be opened and lined up against
the side of screen in Windows so that it will
make it half the screen size.
Resolution used: 1366x768


"""

# Globals
# --------------------------------------------

x_pad = 7
y_pad = 186

from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import os
import time
import win32api, win32con

class Cord:

    b_boutique = (184,174)
    b_cafe = (262, 174)
    b_burgerHouse = (347, 174)
    b_nightClub = (430, 174)
    b_hotel = (506, 174)
    b_material = (184, 318)
    b_energy = (262, 318)
    b_food = (347, 318)
    b_iron = (430, 318)
    b_technology = (506, 318)

    business = [b_boutique, b_cafe, b_burgerHouse, b_nightClub, b_hotel, b_material, b_energy, b_food, b_iron, b_technology]

    b_buy_max = (610, 339)
    u_buy_max = (314, 336)
    c_buy_max = (336, 341)
    a_buy_max = (556, 340)
    p_buy_max = (92, 344)
    
    o_claimFee = (432, 156)
    o_startOver = (406, 273)

    close = (637, 29)

    upgrades = (32, 140)
    events = (104, 140)
    cityFacilities = (32, 210)
    atomicLab = (104, 210)
    port = (32, 278)
    airport = (104, 278)
    trophies = (32, 347)
    office = (104, 347)

    c_material = (162, 84)
    c_energy = (336, 84)
    c_food = (504, 84)

class Color:

    orange_available = (255, 162, 0)

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+667, y_pad+376)
    im = ImageGrab.grab(box)
    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('click')

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left up')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def startGame():
    #start Muted Game
    mousePos((334, 273))
    leftClick()
    time.sleep(.1)

    #offline earnings skip
    mousePos((334, 320))
    leftClick()
    time.sleep(.1)

    #increase buy business to max
    for i in range(3):
        mousePos(Cord.b_buy_max)
        leftClick()
        time.sleep(.1)

def buyBusiness(index):
    s = screenGrab()
    if s.getpixel(Cord.business[index]) == Color.orange_available:
        print('it is available')
        mousePos(Cord.business[index])
        leftClick()
        time.sleep(.1)

def buyBusinesses():

    for i in range(10):
        buyBusiness(i)


def buyUpgrades():
    mousePos(Cord.upgrades)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.u_buy_max)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.close)
    leftClick()
    time.sleep(.1)

def buyCityFacilities():
    mousePos(Cord.cityFacilities)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.c_material)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.c_buy_max)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.c_energy)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.c_buy_max)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.c_food)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.c_buy_max)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.close)
    leftClick()
    time.sleep(.1)

def buyAtomicLab():
    mousePos(Cord.atomicLab)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.a_buy_max)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.close)
    leftClick()
    time.sleep(.1)

def buyPort():
    mousePos(Cord.port)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.p_buy_max)
    leftClick()
    time.sleep(.1)

    mousePos(Cord.close)
    leftClick()
    time.sleep(.1)

def playGame():
    for i in range(5):
        buyBusinesses()
        time.sleep(1)
    #create checks for color of availability
    buyCityFacilities()
    buyUpgrades()
    buyAtomicLab()
    buyPort()

def main():
    startGame()
    while True:
        playGame()

if __name__ == '__main__':
    main()
