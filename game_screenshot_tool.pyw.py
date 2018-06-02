"""
The game must be opened and lined up against
the side of screen in Windows so that it will
make it half the screen size.
Resolution used: 1366x768

//STOPPED on step 7
"""

# Globals
# --------------------------------------------

x_pad = 7
y_pad = 186

from PIL import ImageGrab
import os
import time

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+667, y_pad+376)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
