# -*- coding: utf-8 -*-
''' 
Description:
    Sends a sinusoidal signal to the soundcard output 1, 
    records the inputs 1 and 2, and plots them.

Author:
    Antonin Novak
    Le Mans University, FRANCE
'''

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


""" Sound card setup """
print(sd.query_devices())   # show list of devices
sd.default.device = (1, 3)  # set the device numbers (input, output)


""" Parameters """
fs = 48000                  # sample rate [Hz]

""" sine signal """
T = 2       # time duration of the sine signal [s]
f0 = 500    # frequency of the sine signal [Hz]

t = np.arange(0, T, 1/fs)
x = np.sin(2*np.pi*f0*t)

""" play and record simultaneously """
y = sd.playrec(x,  # x is the signal to be played by the sound card
               samplerate=48000,
               channels=2,
               output_mapping=(1),  # output channel 1
               input_mapping=(1, 2),  # input channels 1 and 2
               blocking=True  # wait until playback is finished
               )

# separate the channels
y1 = y[:, 0]  # channel 1
y2 = y[:, 1]  # channel 2

fig, ax = plt.subplots()
ax.plot(t, y1)
ax.plot(t, y2)
ax.set(xlabel='Time [s]', ylabel='measured signals')

plt.show()
