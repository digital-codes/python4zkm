import pygame
import random

import zkmconst as z

# run a simple game of life
# you can set new pixels by clicking into the fields

# ##########################
# this is a lengthy class definition
# but you can jump to the end of the "calc" function
# directly and check/edit the fundamental rules of the game ...


class Gol(pygame.sprite.Sprite):
    def __init__(self,x,y):
        ### init with index
        super(Gol, self).__init__()
        self.x = x
        self.y = y
        # size of the tile
        self.l = min(z.scr[0],z.scr[1]) // z.gs
        self.surf = pygame.Surface((self.l - 1, self.l - 1))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(left = 1 + self.x*self.l, \
                                       top = 1 + self.y*self.l)

    def on(self):
        ### set value to 1
        self.v = 1
        self.surf.fill((255,255,255))

    def set(self):
        ### set value from matrix
        self.v = z.ga[self.x][self.y]
        if self.v > 0:
            self.surf.fill((255,255,255))
        else:
            self.surf.fill((0,0,0))

    def update(self):
        ### update matrix
        z.ga[self.x][self.y] = self.v

    def calc(self):
        ### compute new value
        # compute sum of neighbours
        s = self.v
        if self.x > 1:
            s += z.ga[self.x - 1][self.y]
        if self.x < z.gs - 1:
            s += z.ga[self.x + 1][self.y]
        if self.y > 1:
            s += z.ga[self.x][self.y - 1]
        if self.y < z.gs - 1: 
            s += z.ga[self.x][self.y + 1]
        # decide how to move on. don't use >
        # makes too much active squares
        # 2 works well
        # 4 works well too
        # you can add more complicated things like
        # birth ...
        # #################################################
        # here comes the fundamental rule of the game ...
        # self.v = 1 if s == 2 or s == 4 else 0
        self.v = 1 if s == 2 else 0
        # #################################################

# #################################################
def main():
    pygame.init()
    screen = pygame.display.set_mode((min(z.scr[0],z.scr[1]),\
                                      min(z.scr[0],z.scr[1])))
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    #create and initialize the tiles
    tiles = []
    for x in range(z.gs):
        for y in range(z.gs):
            z.ga[x][y] = 1 if random.randint(0,4) > 2 else 0
            tile = Gol(x,y)
            tile.set()
            tiles.append(tile)

    # this is the core loop
    # in each iteration it checks for events like
    # mouse clocks or key input
    # it copies the background
    # it computes all pixels
    # and checks for user stimulations
    # then it updates all pixels
    # finally it draws all pixels with the updated values
    # after a short delay the loop repeats
    # this is a basic procedure in all interactive programs
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
        # background
        screen.blit(background, (0, 0))
        # compute new values on all tiles
        for t in tiles:
            t.calc()
            # allow to activate tiles manually
            if pygame.mouse.get_pressed()[0] and \
               t.rect.collidepoint(pygame.mouse.get_pos()):
                t.on()

        # update all values. don't merge this with calc!
        for t in tiles:
            t.update()
            t.set()
            screen.blit(t.surf, t.rect)

        # show and wait            
        pygame.display.flip()
        pygame.time.delay(300)

    print("end")
    

# #################################################
# this is where the program starts
# #################################################
if __name__ == "__main__":
    main()
    
