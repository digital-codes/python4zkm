# OpenCodes
## The world as a field of data
*German translation - done by [Google](https://translate.google.de) - of this text [here](./opencodes_de.txt)*

The exhibitions [OpenCodes](https://zkm.de/en/exhibition/2017/10/open-codes) at the [ZKM](https://open-codes.zkm.de/en), Karlsruhe, Germany, shows a broad range of digital artworks. For an computer engineering expert like me many (but not all) of the underlying approaches, algorithms or implementations are commonplace. However, the creative processes expressed in the artworks are nevertheless fascinating and inspiring.

In this project I try to show some technical background of the installations on display by presenting a collection of programming examples related to different aspects of the digital works.
The programming is based upon the language [Python3](https://www.python.org/). Python is freely available for all major platforms and is quite powerfull while still easy to understand and learn.

Digital artworks typically make use of technical interfaces to communicate with the observers - or users. These interfaces translate from digital signals - in other words: numbers - generated by the machinery built by the artist - normally some kind of computer - to human senses. For example, a video screen, a digital audio encoder, a virtual or augmented reality system. Some interfaces translate in the other direction by sensing human activities. They create numbers from physical motion of our body or from our brain activity. The more complete the translation and the better the quality the more "real" is our interaction with the digital objects. 

But there are also a number of works which do not use digital interfaces directly but traditional media like paper printings or written text. Still they demonstrate aspects of our digital surroundings - often results of "artificial intelligence" (AI): 	machines doing things like we do.

To make AI work, enormous amounts of data have to be fed into machine learning algorithms so they learn over time what we cannot teach them directly in the traditional form of imperative algoriithms (programs). Data is becoming more and more important as a means to develop the tools of the digital age. It is obvious that the term "Knowledge is Power" has a brand-new meaning in todays world. As data is knowledge, allowing private property on data at a large scale is a big risk for democracy. We have to think about this, seriously.
The OpenCodes exhibition has a strong focus on data, in particular during its second phase called "The World as a Field of Data". OpenCodes also targets education on the core digital topics: data and code. This project aims to help in this education.

Not all of our human senses can equally well be interfaced by digital technology. However for our primary senses of vision and hearing it works quite well. Also our "symbolic sense" (which isn't one of the typical senses) is a very good candidate: human language in written form was used even before the two from above and machines start to talk and understand what we say. 
Interfaces to taste, smell, skin sensing and balance are by far not on-par with the others.

## Artworks and Topics
The topic "data" is introduced by the installation of <a name="dfield">Weibel and Lölkes</a>: [The World as a Field of Data](https://zkm.de/de/ausstellung/2017/10/open-codes). Data are taken from a large number of publicly available feeds and displayed in a (more or less) uniform style.

<img src="../data/fieldOfData.jpg" width="250" style="margin-left:50px">
<!--  no longer available:
<img src="https://scontent-frt3-1.xx.fbcdn.net/v/t1.0-9/40661157_10155767726086964_5582587217051648000_o.jpg?_nc_cat=0&oh=04b91aae92a54735eaaacc33b5484c29&oe=5C1DB4BC" width="250" style="margin-left:50px">
-->

> The vast number of electronic interfaces like smartphones, computers, and screens, which accompany people every day in doctors’ surgeries, at home, in offices, at the stock exchange, airports, or railway stations, is overwhelming proof that navigating by the sun, moon, and stars has long since been replaced by satellites and other technological instruments. People living in the digital age don’t navigate by the position of the stars and sun; they follow where digital devices lead them, which receive information from the cell tower on the horizon and orbiting satellites in space. The installation The World as a Field of Data confronts us with this field of data that accompanies us around the clock in a deliberately exaggerated way. Data fields are omnipresent. All the information that is generated as a result of our interaction on the Net and in the real world are assembled on around 40 screens, which hang in the air as a data cloud at ZKM’s Atrium 8.
 
 Refik Anadol uses EEG-data from a human brain to generate an optical visualization in [Melting Memories](https://zkm.de/de/melting-memories). This requires advanced visualization techniques and demonstrates a variety of contexts in which we can use the same data. 
 
 <img src="https://www.thisiscolossal.com/wp-content/uploads/2018/04/brain-og-2.jpg" width="250" style="margin-left:50px">
 
> Melting Memories debuts new advances in technology that enable visitors to experience aesthetic interpretations of motor movements inside a human brain. The work grows out of the artist’s experiments with the advanced technology tools provided by the Neuroscape Laboratory at the University of California, San Francisco. Neuroscape is a neuroscience center focusing on technology creation and scientific research on brain function of both healthy and impaired individuals. Anadol gathers data on the neural mechanisms of cognitive control from an EEG (electroencephalogram) that measures changes in brain wave activity and provides evidence of how the brain functions over time. These data sets constitute the foundation for the unique algorithms that the artist needs for the multidimensional visual structure on display.

<a name="stock">Rybn</a> used a fairly traditional display style of stock market data to introduce their special codes for trading algorithms used in [ADM-XI](https://zkm.de/de/adm-xi). This is also a very good example for fundamentals of programming.

<img src="https://zkm.de/media/styles/r17_720_dynamic/public/bild/372-adm-xi.png?itok=vqFUenkN" width="250" style="margin-left:50px">

>ADM XI is an independent research platform for experimental algorithmic trading engineering that challenges the dogma of neoclassical economics. It created a collection of heretic, irrational, and experimental operating trading algorithms that are released to compete with each other on a marketplace hosted and organized by RYBN.ORG. In this contest, benefits are no longer driven by prices and other economic instruments, but by living organisms – soil, plants, bacteria; by supraterrestrial laws – environmental, astronomical, astrological; and by ancient or forbidden knowledge – esoterica, magic, geomancy. All the algorithms follow their own non-mercantile and obsessive logic: some attempt to produce total and irreversible chaos; others try to influence market prices to make them look a given geometric shape. 

<a name="quade">Jörn Müller-Quade</a> gives a close combination of math and visual art with [Code Beautiful like a Clock](https://zkm.de/de/code-beautiful-like-a-clock). Only a few lines of code are needed to generate images of particular beauty.

<img src="https://zkm.de/media/styles/r17_720_dynamic/public/bild/344-code-beautiful-clock.jpg?itok=WzJHJ-0B" width="250" style="margin-left:50px">

>Many people find mechanical clocks appealing. No such aesthetic appeal is ascribed to computer programs, although they are mechanical in a similar way: fixed, predefined commands are executed to yield a result. The “mechanics” of computer programs play out on a time scale that lies outside of human perception. While many programs have reaction times that are perceptible to us, basic commands are completed a billion times faster during this time. This work is intended to bridge these extreme time scales, making it possible to experience the mechanical character of computer programs. The exhibit is composed of three units: on the left is the program code, with an emphasis on the command that is being executed at a given moment. In the middle, the “inner life” of the processor with its registers, execution unit and memory is displayed in the act of executing a basic command. On the right, the result is visualized. A control knob changes the processing speed: when it is slowed down, individual steps become discernible, but their visible result is delayed. At a high speed, the result appears quickly, but the processor’s individual steps can no longer be observed.

<a name="gol">Algorithmic structures</a> generating features similar to living organism are visualized in [Game of Life](https://zkm.de/de/game-of-life) by Christian Lölkes. 

<img src="https://zkm.de/media/styles/r17_720_dynamic/public/bild/334-game-life.jpg?itok=CsbmFelY" width="250" style="margin-left:50px">

>In Conway’s Game of Life, a population simulation is carried out by a cellular automaton on a two-dimensional playing field according to a certain set of rules. The rules consist of four specifications that are applied depending on the number of neighbors (standard values): birth (an empty cell has exactly three neighbors), living on to the next generation (a live cell has two or three neighbors), death by loneliness (a cell has fewer than two living neighbors) and death by overcrowding (a cell has more than three living neighbors). This set of numbers provides the foundation for periodic structures to appear, run their course, and their termination. This simulation is also used in other areas, including in business and in the natural sciences. 

A more complex algorithm - <a name="sos">sorting</a> of data - with simple graphics is combined with musical expression of the algorithmic procedure in [Sound of Sorting](https://zkm.de/de/sound-of-sorting) by Christian Lölkes. 

<img src="https://zkm.de/media/styles/r17_720_dynamic/public/bild/335-sound-sorting.jpg?itok=rEyYH3zq" width="250" style="margin-left:50px">

>Sorting processes are essential components of codes and algorithms in their everyday processing of data. They bring order to the data sets that is based on values and parameters, which they had received beforehand. Unlike humans, who solve such tasks in a way that is slower, more intuitive, and mainly visual, computers are challenged to execute tasks with maximum efficiency in terms of time, storage, and resources. For example, these processes sort search results by hit ratios, transport routes according to distance, or workflows by dependency on one other. Each process reaches the same goal with different procedures. If one then associates a sound with each data set and plays it, as soon as the sorting process edits this data set, unique rhythms and melodies emerge.

Daniel Heiss' [Cryptolab](https://zkm.de/de/kryptolab) has math as its primary topic: algorithms and machines used for bitcoin mining. Although complex and (often) energy-hungry the related block-chain mechanism is widely used in commercial projects.

<img src="https://zkm.de/media/styles/r17_720_dynamic/public/bild/425-kryptolab.jpg?itok=UODWEf8j" width="250" style="margin-left:50px">

>Mining is the process that is used to generate cryptographic currencies such as Bitcoin. Performing a Bitcoin transaction requires that hash values meeting certain requirements be found using bruteforce methods. After this hash value has been discovered, a new block of transactions is added to the blockchain. The first miner who finds a given hash value is also rewarded with a specified quantity of newly generated Bitcoins. The combined computing power of all miners taking part in the Bitcoin network is now many times greater than that of the world's TOP500 supercomputers. In »KryptoLab«, prospecting for digital gold takes place live on various forms of hardware. Here the rapid development of the hardware, from a simple workplace computer to a highly specialized ASIC miner from China, can also be traced. At a one-shot miner that was specially developed for the exhibition, visitors can press a button to try their luck at mining a block themselves and perhaps winning 12.5 Bitcoins as their reward. The odds of doing so, however, are far lower than the chances of winning the lottery. The values generated by the miners in »KryptoLab« are being made available to visitors in a series of workshops as part of the exhibition so that visitors can try out interacting with this abstract medium themselves.

<a name="trap">James Bridle's</a> [Autonomous Trap](https://zkm.de/de/autonomous-trap-001) is a preview on future self-driving cars and the problems we have to expect. The fundamental challenge of autonomous driving basically is: making sense out of the massive amount of data generated by the car's sensors. The machine has to understand what it sees.

<img src="https://zkm.de/media/styles/r17_720_dynamic/public/bild/autonomoustrap_jamesbridle.jpg?itok=ftr4AU60" width="250" style="margin-left:50px">

## Code examples
All code samples are in the [source](../src) folder. Files ending with .py are pure Python3 files. Open them with an editor or an IDE like idle3. There are also 3 notebooks, ending with .ipynb, which are Python3 in a more convenient format for learning. The tool [jupiter-notebook](https://jupyter.org/) is required to open them.

Credits go to a large number of people who shared their ideas on publicly availably platforms (like this one) so I could go ahead and include or adapt code fragments together with my own ideas. Credits also go to Ernst Jandl (rights probably owned by [Luchterhand](https://www.randomhouse.de)) for the poem [Ottos Mops](../data/otto.txt) and to [Larva Labs](https://www.larvalabs.com/cryptopunks) for the [punk image](../data/punk.png). The files are copied from the depth of the internet. While giving nice results in the examples, they are neither very special, unique nor important and you can replace them with any other text or image you may find or create. Finally thanks to the person who posted the nice picture of his or her [mops dog](../data/ottos-mops.png) somewhere (I forgot where I got it from). Again, feel free to replace it with you favorite pet (make sure to get the poem right too).

We start with a more general [excursion on data](../src/1-basicData.py) and their possible "interpretations". The basics of [Python programming](../src/2x-basicPython.py) are listed in a lengthy example covering the topics variables, operations, input/output, data types, functions and loops. You can get full documentation about Python [here](https://docs.python.org/3.6/) and on many other sites. More compact and practical examples as introduction to algorithms and programming are [CheckerBoard1](../src/2a-chessPrint.py), [CheckerBoard2](../src/2b-chessList.py), [CheckerBoard3](../src/2c-chessNp.py) all dealing with creating a simple pattern and the [text version of game-of-live](../src/2d-gol-text.py). This is the foundation for the graphical version later on.

This is followed by some simple [2D-graphics](../src/3-simpleGraphics.py) because graphics is the most dominant interface. The graphics area is then further expanded introducing [colors](../src/4-colorGraphics.py), fundamental [image processing, animations and movies](../src/6-punk.py). We link more complex image processing with the [autonomous trap](../src/7-trackSegment.py) and finally create a movie of the [beautiful Julia-set](../src/8-juliaMovie.py) 

The topic of creating patterns using graphics is further expanded following a ZKM workshop on [vernacular algorithms](https://zkm.de/de/veranstaltung/2018/11/from-beadwork-to-coding-vernacular-algorithms-workshop) with [a triangle pattern code](../src/4b-beadwork.py) for a beadwork like this one

<img src="../data/beads.jpg" width="250" style="margin-left:50px">

We can use different algorithm to create such patterns, for example focusing on how to [create the patterns](../data/bead_ani_tri.mp4) or how to [line up the beads](../data/bead_ani_lin.mp4). We can also do [3D visualizations](../data/bead3d.webm)

<img src="../data/bead3d.png" width="250" style="margin-left:50px">

using a 3D rendering program like [Povray](https://povray.org/). 

We studiy the principles behind [Game of life](../src/9-gol.py) and [Sound of Sorting](../src/10-soundOfSort.py) in brief examples. Despite including advanced programming mechanisms, the code should be fairly straightforward.

Encryption utilities are used to create a very simple [block-chain](../src/13-blockchain.py), which could be even used to sign objects created with these exercices.

We learn how to get and show data from the [stock-market](../src/14-stockParse.py) and other sources like news [feeds](../src/15-dataFeeds.py).

Advanced topics cover [music](../src/16-shepardScale.py), [webcam](../src/12-camGrab.py) and [movie generation with sound](../src/11-surfVideo.py).

