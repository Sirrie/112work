import pyaudio
import wave
from Tkinter import *

CHUNK = 1024


wf = wave.open("cello.wav", 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

for e in xrange(12):

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()