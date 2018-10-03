from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

im1 = Image.new("L", (100, 100))
im2 = Image.new("RGB", (100, 100))

draw = ImageDraw.Draw(im1)
draw.rectangle((33, 0, 66, 100), fill=(64))
draw.rectangle((67, 0, 100, 100), fill=(128))
draw.arc([(30,30),(50,50)],0,360,255)

# get a font
#fnt = ImageFont.truetype('Arial.ttf', 40)
#fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
#fnt = ImageDraw.ImageDraw.getfont()
# get a drawing context
#d = ImageDraw.Draw(txt)

fnt = ImageFont.load_default() #("arial.pil")

# draw text, half opacity
#d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
#d.text((10,60), "World", font=fnt, fill=(255,255,255,255))
draw.text((10,60), "World", font=fnt, fill=(255))

#automatically converted to numpy array
plt.imshow(im1, cmap="gray",clim=(0,255))
plt.show()

draw = ImageDraw.Draw(im2)
draw.rectangle((0, 33, 100, 66), fill=(0, 255, 0))
draw.rectangle((0, 67, 100, 100), fill=(255, 0, 0))

draw.ellipse((20, 20, 60,80), fill=(255, 255, 0), outline=(255,255,255))

plt.imshow(im2)
plt.show()

#########
##PIL.ImageDraw.ImageDraw.ellipse(xy, fill=None, outline=None, width=0)
##PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
##PIL.ImageDraw.ImageDraw.point(xy, fill=None)
##PIL.ImageDraw.ImageDraw.polygon(xy, fill=None, outline=None)
##PIL.ImageDraw.ImageDraw.rectangle(xy, fill=None, outline=None, width=0)
##PIL.ImageDraw.ImageDraw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left", direction=None, features=None)
##PIL.ImageDraw.ImageDraw.multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left", direction=None, features=None)
##PIL.ImageDraw.ImageDraw.textsize(text, font=None, spacing=4, direction=None, features=None)
##PIL.ImageDraw.ImageDraw.multiline_textsize(text, font=None, spacing=4, direction=None, features=None)
##PIL.ImageDraw.floodfill(image, xy, value, border=None, thresh=0)
##PIL.ImageDraw.ImageDraw.chord(xy, start, end, fill=None, outline=None, width=0)
##PIL.ImageDraw.ImageDraw.arc(xy, start, end, fill=None, width=0)
##PIL.ImageDraw.ImageDraw.getfont()

