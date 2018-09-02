import io
import numpy as np
import matplotlib.pyplot as plt
import time
#for windows speech, we need win32 stuff 
import os
if "windows" in os.name.lower():
    import win32api
    import win32com.client
import pyttsx3;

# on linux, there is a warning about the default event loop.
# ignore!
import warnings
warnings.filterwarnings('ignore', 'Using default event loop*',)

###########################
with open("otto.txt","r",encoding="iso-8859-15") as infile:
#with open("anders.txt","r",encoding="iso-8859-15") as infile:
     otto = infile.read()
     
infile.close()

obuf = io.StringIO(otto)

npoem = []
nl = []

for o in obuf:
    # strip newlines
    if o == "\n":
        continue
    # this makes a bytearray which will be processed nicer
    ob = bytearray(o.upper().rstrip(),"iso-8859-15")
    npoem.append(ob)
    nl.append(len(ob))

ml = max(nl)

print("Lines:",len(npoem),"\nMaxlen:", ml)


for i in range(len(npoem)):
    for j in range(ml - len(npoem[i])):
        npoem[i].extend(b" ") 

##################################################
# prepare speach
engine = pyttsx3.init();
voices = engine.getProperty('voices')
for v in voices:
    #print("voice:",v.name)
    if "german" in v.name.lower(): #"german":
        engine.setProperty('voice', v.id)
        engine.setProperty("rate",150)
        break


##################################################
plt.ion() # don't use interactive mode here
# unless showing line by line
#plot = plt.figure()
plot = plt.subplot(2,1,1)
x = plt.xticks(np.arange(0,ml, 1.0))
tplot = plt.subplot(2,1,2)
tplot.axis('off')

plt.show()
for i in range(len(npoem)):
    plot.plot(npoem[i],drawstyle='steps-post',linestyle="dotted")
    tplot.clear()
    tplot.axis('off')
    tplot.annotate(npoem[i].decode("iso-8859-15"),\
        xy=(1, 1), xytext=(.96,.94), xycoords="data", \
        textcoords="axes fraction",ha="right", va="top", size=20)
    
    #plt.fill_between(x, 0, npoem[i],clip_on = True)
    plt.draw()
    plt.pause(.01)
    engine.say(npoem[i].decode("iso-8859-15"));
    engine.runAndWait()
    plt.pause(.3)
    #time.sleep(.3)

#plt.close(plot)
