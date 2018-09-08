# python4zkm
Introductionary Python3 samples related to the very basics of data and visualization.

Inspired by and used during an "action-tour" at the "open codes" exhibition at the ZKM, Karlsruhe, Germany

See https://open-codes.zkm.de/en

Tu run all samples you need to install the following modules:

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
  * cv2

In addition, you need the following packages in your system installation:

  * espeak for text to speech output
  * OpenCV3 for image processing
  *  * This is only required for on sampe (trap). It also requires the presence of a
  *  * basic VisualStudio installation. Please refer to the OpenCV3 tutorials like
  *  * here: https://docs.opencv.org/master/d3/d52/tutorial_windows_install.htm
  *  For stockParse you need an API key from Quandl (the stock data provider)
  *  * Sign up for a free key at https://quandl.com and add the key to a file
  *  * private.py with the content:
  *  * * quandl_key = "<the key you got from quandl>"
  *  * stockParse imports the key from this private file

The samples have been tested on Linux and Windows using Python3 version 3.6

Testing image embedding ...

This should work on external urls like

`` ![Bilby Stampede](http://example.com/images/logo.png)

and on internal (relative) urls like

``  ![Image](../blob/master/public_html/img/nokia.png?raw=true)

Image via external URL:

![Img Test](https://github.com/digital-codes/python4zkm/blob/master/data/github.png)

Image via relative URL:

![Internal Img Test](../master/data/github.png?raw=true =200x200)


Via HTML:

<img src="https://github.com/digital-codes/python4zkm/blob/master/data/github.png" width="200">






