#from https://github.com/captbaritone/eldredge-shepard_tone/blob/master/shepard_tone.ly
##"""
##
##\version "2.10.10"
##notes = { c8 cis d dis e f fis g gis a ais b }
##instrument = \set Staff.midiInstrument = "pad 8 (sweep)"
##scale = \new Staff { \instrument \unfoldRepeats { \repeat volta 50 { \notes } } }
##
##
##
##\score {
##	\relative c,,,,, {
##		<<
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##			\scale
##		>>
##	}
##	\midi {
##		\context {
##			\Score tempoWholesPerMinute = #(ly:make-moment 75 4)	
##		}
##	}
##}
##
##"""

# from https://github.com/evpu/Shepard-tone-music21


# ************************************************************************
# Shepard tone with music21
# https://github.com/evpu
# ************************************************************************

import os
from music21 import stream, instrument
from music21.note import Note

print(os.getcwd())
os.chdir('.')  # set working directory

loop = 10
length = 0.5

# Highest octave, volume gets lower
shepard_tone_u = stream.Part()
shepard_tone_u.insert(0, instrument.Piano())
c_major = ['C#5', 'D#5', 'E#5', 'F#5', 'G#5', 'A#5', 'B#5', 'C#6', 'D#6', 'E#6', 'F#6', 'G#6', 'A#6', 'B#6']
for l in range(loop):
    volume_increment = 0
    for i in c_major:
        n = Note(i, quarterLength=length)
        n.volume.velocityScalar = 0.7 - volume_increment
        shepard_tone_u.append(n)
        volume_increment = volume_increment + 0.05

# Middle octave, volume constant
shepard_tone_m = stream.Part()
shepard_tone_m.insert(0, instrument.Piano())
c_major = ['C#3', 'D#3', 'E#3', 'F#3', 'G#3', 'A#3', 'B#3', 'C#4', 'D#4', 'E#4', 'F#4', 'G#4', 'A#4', 'B#4']
for l in range(loop):
    for i in c_major:
        n = Note(i, quarterLength=length)
        shepard_tone_m.append(n)

# Lowest octave, volume gets higher
shepard_tone_l = stream.Part()
shepard_tone_l.insert(0, instrument.Piano())
c_major = ['C#1', 'D#1', 'E#1', 'F#1', 'G#1', 'A#1', 'B#1', 'C#2', 'D#2', 'E#2', 'F#2', 'G#2', 'A#2', 'B#2']
for l in range(loop):
    volume_increment = 0
    for i in c_major:
        n = Note(i, quarterLength=length)
        n.volume.velocityScalar = 0.05 + volume_increment
        shepard_tone_l.append(n)
        volume_increment = volume_increment + 0.05


shepard_tone = stream.Stream([shepard_tone_u, shepard_tone_m, shepard_tone_l])

shepard_tone.write('midi', 'shepard.mid')

print("Synthesizing")
from midi2audio import FluidSynth
# using the default sound font in 44100 Hz sample rate
# we must specify the sound font, the default points 
# to the wrong directory
#fs = FluidSynth(sound_font="/usr/share/soundfonts/epiano.sf2")
fs = FluidSynth(sound_font="/usr/share/soundfonts/default.sf2")
fs.midi_to_audio('shepard.mid', 'shepard.wav')

