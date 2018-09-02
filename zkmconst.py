# constants
import pygame # for events

scr = 600,400 # scrren size

# sound of sorting
nkeys = 13 # number of keys 
SNDEVNT = pygame.USEREVENT + 1  # sound event
TMREVNT = pygame.USEREVENT + 2  # timer events
sorting = 0

# game of life
gs = 16 # cols by rows
# matrix of size gs x gs
ga = [[0 for c in range(gs)] for r in range(gs)]



