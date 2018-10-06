# python4zkm
Introductionary Python3 samples related to the very basics of data and visualization.

Inspired by and used during an "action-tour" at the "open codes" exhibition at the 
[ZKM](https://open-codes.zkm.de/en), Karlsruhe, Germany


<img src="https://zkm.de/media/styles/r17_1280/public/bild/ocii_plakat_dina1_final.jpg?itok=77xfS05w&c=e425af2cad7290dca592b01cdf1b1ca4" width="250">

More information on the related artworks is be in the [docs folder](../doc/opencodes.md)

To run all samples you need to install the following modules:

  * numpy
  * matplotlib
  * numba
  * pygame
  * random
  * pyttsx3
  *  * On Windows you need pywin32 too for speech 
  * feedparser
  * hashlib
  * html2text
  * quandl
  * wave
  * moviepy
  * vispy
  * imageio
  * scikit-image
  * sxipy
  * PIL (aka PILLOW)
  
I hope I got all of them. In case I didn't you will get a warning about missing modules....  


In addition, you need the following packages in your system installation:

  * espeak for text to speech output
  * Image processing examples qould profit from opencv2, but this requires a lot of additional stuff on WIndows, so I tried to avoid it. In case you want to go that way:
  * * Install OpenCV3
  * * Get a basic VisualStudio installation. Please refer to the OpenCV3 tutorials like
  *  * * here: https://docs.opencv.org/master/d3/d52/tutorial_windows_install.htm
  *  For stockParse you need an API key from Quandl (the stock data provider)
  *  * Sign up for a free key at https://quandl.com and add the key to a file
  *  * private.py with the content:
  *  * * quandl_key = "<the key you got from quandl>"
  *  * stockParse imports the key from this private file

The samples have been tested on Linux and Windows using Python3 version 3.6



