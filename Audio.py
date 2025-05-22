

import math
import numpy
from scipy.io import wavfile

kammertonA =  [ 10000*math.sin(2*440*math.pi*x/44100) for x in range(0,5*44100)]

def writeWav( fn, ds):
  wavfile.write(fn,44100,numpy.array(list(map(lambda x:numpy.int16(round(x)),ds))))

def w1(): writeWav("kammertonA.wav", kammertonA)

def kammertonA2():
  return [10000*math.sin(2*440*math.pi*x/44100)+5000*math.sin(2*880*math.pi*x/44100)
             for  x in range(0,10*44100)]

def w2():writeWav("kammertonA2.wav", kammertonA2())

def pluggedTime( t, wv): # x=t Abtastrate, i = Anzahl der Obertöne wv = ?
  return [
    (10000 * 0.5 ** (x // 5000)) * sum((1 / i) * math.cos(2 * math.pi * (x / wv) * i) for i in range(1, 11))
    for x in range(t)
]

def pluggedH(x):return pluggedTime(44100//2,x)
def plugged(x): return pluggedTime(44100,x)
def pluggedD(x): return pluggedTime(2*44100,x)

def kammertonAHarmonics(): return plugged(110)

def w3(): writeWav( "pluggedA.wav", kammertonAHarmonics())

a = 440
b = 493.88
cs= 554.37
d = 587.33
e = 659.25
fs= 739.99
gs= 830.61
aP= 880.00

def scale(): return []

def w4(): writeWav( "scale.wav", scale())

def maj7(): return  []

def w5():  writeWav( "maj7.wav", maj7())

def getWavFromFile( fn ) : return list(wavfile.read(fn)[1])

def abtast():
   x = 0
   while (True):
     yield x
     x += 1/44100

def toPgfplot( ws ): return ""

def writeForLaTeX(resultFileName, ws):
  start = "\\begin{tikzpicture}\n"\
          "\\begin{axis}\n"\
          "[axis lines = left,xlabel = $Sekunde$,ylabel = {Samples},]\n"\
          "\\addplot[color=blue,mark=dot,]\n"\
          "\\coordinates {\n"
  end= "};\n"\
       "\\end{axis}\n"\
       "\\end{tikzpicture}"
  f = open(resultFileName, "w")
  f.write (start)
  f.write(toPgfplot(ws[:441]))
  f.write(end)
  f.close()

import cmath

def dft(xs): return []

def stepFrom0(n):
   x = 0
   while (True):
     yield x
     x += n

def analyseFileStart( fn ):
  ws = getWavFromFile(fn)
  return  zip(stepFrom0(10)
             ,map (lambda x:abs(x).real,dft(list(map(lambda x: complex(0,x),ws[:4410])))[:200]))

if __name__ == "__main__":
  w3()