'''
Configuration for aspect ratio and frame rate of the game
'''
import pygame
from sprites import *

WIN_WIDTH = 800
WIN_HEIGHT = 600
TILESIZE = 32
FPS = 60

BLOCKS_LAYER = 2
GROUND_LAYER = 1

BLACK = (0,0,0)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'BB.................B',
    'BBBB...............B',
    'BBB...............BB',
    'BBBB.............BBB',
    'B...............BBBB',
    'B..............BBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..............BBBBB',
    'B..BBBB..........B.B',
    'B..................B',
    'BB................BB',
    'BBB..............BBB',
    'BBBBBBBBBBBBBBBBBBBB',

    ]