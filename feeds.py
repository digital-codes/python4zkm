import feedparser
import html2text

import numpy as np
import pylab as plt
import time


# html to text parser
hp = html2text.HTML2Text()
hp.ignore_images = True
hp.ignore_emphasis = True
hp.ignore_links = True

#tazfeed = "http://www.taz.de/!s=rss/"

tazfeed = "http://taz.de/Themen-des-Tages/!p15;rss/"

stockfeed = "https://boerse.ard.de/index~rss.xml"

newsfeed = "http://www.tagesschau.de/xml/rss2"

ntvfeed = "https://www.n-tv.de/rss"

###################
# if pylab not present the comment the import and this function
def show(s):
    plt.annotate(s, xy=(1, 1), xytext=(.96,.94), xycoords="data", textcoords="axes fraction",ha="right", va="top")
    plt.axis('off')
    plt.show()

###################
feed = feedparser.parse( tazfeed )
#print(feed)
print("----------------------------")
print("TAZ\n\n")

# show just 1 in a window
wincnt = 1
for e in feed.entries:
    print(e.date, e.title)
    for c in e.content:
        if c.type == "text/html":
            print(hp.handle(c.value))
            if wincnt > 0:
                show(hp.handle(c.value))
                wincnt -= 1
            
    print("\n\n")
    
#################
feed = feedparser.parse( stockfeed )
#print(feed)
print("----------------------------")
print("ARD Börse\n\n")

for e in feed.entries:
    if hasattr(e,"summary"):
        print(e.published,e.title)
        print(hp.handle(e.summary))
            
    print("\n\n")
    

#################
feed = feedparser.parse( newsfeed )

#print(feed)
print("----------------------------")
print("Tagesschau\n\n")
for e in feed.entries:
    if hasattr(e,"summary"):
        print(e.published,e.title)
        print(hp.handle(e.summary))
            
    print("\n\n")
    
#################
feed = feedparser.parse( ntvfeed )

#print(feed)
print("----------------------------")
print("NTV\n\n")
for e in feed.entries:
    if hasattr(e,"summary"):
        print(e.published,e.title)
        print(hp.handle(e.summary))
            
    print("\n\n")
    
