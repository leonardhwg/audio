import math
import numpy
from scipy.io import wavfile
from datetime import datetime
import os

kammertonA = [10000 * math.sin(2 * 440 * math.pi * x / 44100) for x in range(0, 5 * 44100)]


def writeWav(fn, ds):
  wavfile.write(fn, 44100, numpy.array(list(map(lambda x: numpy.int16(round(x)), ds))))


def w1(): writeWav("kammertonA.wav", kammertonA)


def kammertonA2():
  return [10000 * math.sin(2 * 440 * math.pi * x / 44100) + 5000 * math.sin(2 * 880 * math.pi * x / 44100)
          for x in range(0, 10 * 44100)]


def w2(): writeWav("kammertonA2.wav", kammertonA2())


def pluggedTime(t, wv):  # x=t Abtastrate, i = Anzahl der / Obertöne wv = frequenz
  amplitude = lambda x: 10000 * 0.5 ** (x // 500) # if x >= 5000 else 10000
  return [
     sum((1 / i) * amplitude(x) * math.sin(2 * wv * math.pi * (x / t) * i) for i in range(1, 11))
    for x in range(1, t)
  ]


def pluggedH(x): return pluggedTime(44100 // 2, x)


def plugged(x): return pluggedTime(44100, x)


def pluggedD(x): return pluggedTime(2 * 44100, x)


def kammertonAHarmonics(): return plugged(110)


def w3(): writeWav("pluggedA.wav", kammertonAHarmonics())


a = 440
b = 493.88
cs = 554.37
d = 587.33
e = 659.25
fs = 739.99
gs = 830.61
aP = 880.00
notes = [a,b,cs,d,e,fs,gs,aP]


def scale(): 
     return sum([pluggedH(x) for x in notes],[])



def w4(): writeWav("scale.wav", scale())

chord = [a,cs,e,gs]
def maj7(): 
  ap = pluggedD(a)
  cp = pluggedD(cs)
  ep = pluggedD(e)
  gp = pluggedD(gs)
  res = [0]*(88200)
  
  for i in range(len(ap)):
    res[i] += ap[i]
  for i in range(len(cp)):
    if i + 2000 < len(res):
      res[i+2000] += cp[i]

  for i in range(len(ep)):
    if i + 4000 < len(res):
      res[i+4000] += ep[i]

  for i in range(len(gp)):
    if i + 6000 < len(res):
      res[i+6000] += gp[i]
  return res

  

def w5():  writeWav("maj7.wav", maj7())


def getWavFromFile(fn): return list(wavfile.read(fn)[1])


def abtast():
  x = 0
  while (True):
    yield x
    x += 1 / 44100


def toPgfplot(ws):
  cords = ""
  zeiger = abtast()

  for w in ws:
    cords += "\n(" + str(next(zeiger)) + "," + str(w) + ")"

  return cords[1:]


def writeForLaTeX(resultFileName, ws):
  start =  (
        "\\documentclass[tikz,border=5pt]{standalone}\n"
        "\\usepackage{pgfplots}\n"
        "\\pgfplotsset{compat=1.18}\n"
        "\\begin{document}\n"
        "\\begin{tikzpicture}\n"
        "\\begin{axis}"
        "[axis lines = left,xlabel = $Sekunde$,ylabel = {Samples},]\n"
        "\\addplot[color=blue,mark=dot]"
        "coordinates {\n"
    )

  end = (
        "};\n"
        "\\end{axis}\n"
        "\\end{tikzpicture}\n"
        "\\end{document}\n"
    )

  f = open(resultFileName, "w")
  f.write(start)
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


def analyseFileStart(fn):
  ws = getWavFromFile(fn)
  return zip(stepFrom0(10)
             , map(lambda x: abs(x).real, dft(list(map(lambda x: complex(0, x), ws[:4410])))[:200]))

def logChord():
  xs = maj7()
  name = "log/" + str(datetime.now()) + "_maj.log"
  f = open(name,"x")
  #with open(name, "a") as f:
  for i,x in enumerate(xs):
      if(i%100 == 0):
        f.write(f"[{i}]")
        f.write(str(x))
        f.write("\n")
  writeForLaTeX("latex/maj7.tex",xs)

if __name__ == "__main__":
  logChord()