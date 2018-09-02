import numpy as np
import pygame
import random

import zkmconst as z

# we create a class for the keys, realized with pygame sprites
class Key(pygame.sprite.Sprite):
    def __init__(self,id,sd):
        ### init with index and sound data
        super(Key, self).__init__()
        # key id 
        self.id = id
        # width
        self.w = z.scr[0] // z.nkeys
        # create the surface which will later be drawn
        # leave 2 segments for button
        self.surf = pygame.Surface((self.w - 5, (self.id + 1) * z.scr[1]//(z.nkeys + 2)))
        self.surf.fill((255, 255, 255))
        # copy the sound data to the key instance
        self.sd = sd.copy()
        # create a sound channel
        self.sound = pygame.mixer.Sound(self.sd)

    def set(self,p):
        ### set rectangle and sound data
        self.rect = self.surf.get_rect(left = p*self.w + 2, top = 5)
        
    def play(self):
        ### start playing and return the channel number
        self.ch = self.sound.play()
        self.ch.set_endevent(z.SNDEVNT)
        return self.ch

    def stop(self):
        self.ch.stop()
        self.ch.set_endevent()

def makeKeys(fs):
    ### series of 13 tones, 2 octaves
    T = 1.0 # time in seconds, arbitrary length of tone
    # initialize data array
    t = np.arange(0,T,1/fs)
    keys = []
    # create the sound data: 12 keys for one octave
    # tone distance is 12th root from 2
    for i in range(0,13):
        tn = np.power(2,i/12)
        x = 0.5 * np.sin(2*np.pi*440*tn*t)   # 0.5 is arbitrary to avoid clipping sound card DAC
        x = (x*32768).astype(np.int16)  # scale to int16 for sound card
        # append the key to the list of keys
        keys.append(Key(i,x))
    return keys

# function to show all keys
def showAll(screen,background,keys,r):
    screen.blit(background, (0, 0))
    for i in range(len(r)):
        keys[r[i]].set(i)
        screen.blit(keys[r[i]].surf, keys[r[i]].rect)
        pygame.display.flip()
    pygame.time.wait(2000)
    

def main():
    #sample frequency 8kHz
    fs = 8000 # Hz
    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init(buffer=2) # very small buffer here to reduce latency
    keys = makeKeys(fs)
    
    pygame.init()
    screen = pygame.display.set_mode((z.scr[0],z.scr[1]))
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    # define the random initialisation
    r = []
    idx = -1
    sortIdx = 1
    seed = 1234876
    def randInit(seed):
        random.seed(seed)
        r = [random.randint(0,len(keys)-1) for i in range(len(keys))]
        idx = 0
        sortIdx = 1
        return 0, 1, r

    idx, sortIdx, r = randInit(seed)
    print(idx,sortIdx, r)
    # 
    screen.blit(background, (0, 0))
    clock = pygame.time.Clock()


    #show initial
    showAll(screen,background,keys,r)

    ### main loop
    # this is an interactive loop which responds to events
    # similar to gol
    run = True
    # we use a timer with 100ms resolution to get
    # the same time for all keys
    pygame.time.set_timer(z.TMREVNT,100)
    ch = keys[r[idx]].play()
    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == z.SNDEVNT:
                idx += 1
                if idx == len(keys):
                    idx = 0
                    #here we call the core of the sorting function
                    if sortIdx < len(keys):
                        j = sortIdx
                        while j > 0 and r[j] < r[j-1]:
                            r[j], r[j-1] = r[j-1], r[j]
                            j -= 1
                        print("Sort step: ",sortIdx)
                        sortIdx += 1
                    elif sortIdx == len(keys):
                        #show final
                        showAll(screen,background,keys,r)
                        sortIdx += 1

                ch = keys[r[idx]].play()
            elif event.type == z.TMREVNT:
                ch.stop()

        screen.blit(background, (0, 0))
        keys[r[idx]].set(idx)
        screen.blit(keys[r[idx]].surf, keys[r[idx]].rect)
        pygame.display.flip()
        clock.tick(30)

    print("end")

##############
main()

