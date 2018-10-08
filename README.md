# python4zkm
Introductionary Python3 samples related to digital artworts, demonstrating principles of data, images, sound, and visualizations. 
Inspired by the [open codes](https://open-codes.zkm.de/en) exhibition at the 
[ZKM](https://zkm.de/), Karlsruhe, Germany

The related workshop [Code like an Artist](https://www.meet-and-code.org/de/de/event-show/1872
) ist recognized by the international [meet and code](https://www.meet-and-code.org/de/de/
) program.  

<img src="https://zkm.de/media/styles/r17_1280/public/bild/ocii_plakat_dina1_final.jpg?itok=77xfS05w&c=e425af2cad7290dca592b01cdf1b1ca4" width="250">

More information on the related artworks and the samples is in the [doc folder](../master/doc/opencodes.md)
The code samples don't aim to demonstrate best-practice in terms of coding style and documentation 
(not even on English syntax and grammar). Instead, they try to give an introduction in a very brief manner to
everything from "what is a variable" to "how to crate a movie" and beyond.

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
  * Image processing examples would profit from opencv2, but this requires a lot of additional stuff on WIndows, so I tried to avoid it. In case you want to go that way:
  * * Install OpenCV3
  * * Get a basic VisualStudio installation. Please refer to the OpenCV3 tutorials like
  *  * * here: https://docs.opencv.org/master/d3/d52/tutorial_windows_install.htm
  *  For stockParse you need an API key from Quandl (the stock data provider)
  *  * Sign up for a free key [here](https://quandl.com) and add the key to a file
  *  * private.py with the content:
  *  * * quandl_key = "<the key you got from quandl>"
  *  * stockParse imports the key from this private file

The samples have been tested on Linux and Windows using Python3 version 3.6



