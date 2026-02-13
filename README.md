# python4zkm
Introductionary Python3 samples related to digital artworts, demonstrating principles of data, images, sound, and visualizations. Inspired by the [open codes](https://open-codes.zkm.de/en) exhibition at the 
[ZKM](https://zkm.de/), Karlsruhe, Germany.

The related workshop [Code like an Artist](https://www.meet-and-code.org/de/de/event-show/1872) ist recognized by the international [meet and code](https://www.meet-and-code.org/de/de/) program.

<img src="https://zkm.de/media/styles/r17_1280/public/bild/ocii_plakat_dina1_final.jpg?itok=77xfS05w&c=e425af2cad7290dca592b01cdf1b1ca4" width="250">

More information on the related artworks and the samples is in the [doc folder](../master/doc/opencodes.md).

## Disclaimer

The code samples don't aim to demonstrate best-practice in terms of coding style and documentation (not even on English syntax and grammar). Instead, they try to give an introduction in a very brief manner to everything from "what is a variable" to "how to create a movie" and beyond.

## Requirements

### System installations

- Python 3.6+
- eSpeak
  - for text to speech output
- OpenCV3
  - a basic VisualStudio installation. Please refer to the OpenCV3 tutorials like [here](https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html)
- Quandl API Key (for `stockParse` sample)
  - sign up for a free key [here](https://quandl.com) and add the key to a file `private.py` created in a repository root folder with the following content:
      - `quandl_key = <the key you got from quandl>`

### Python packages

In order to run all samples, you need to install dependencies as follows:

On Windows:

```
pip install -r requirements-win.txt
```

On Linux or Mac:

```
pip install -r requirements.txt
```
