import unittest

from Audio import *

import xmlrunner 
import math

ws1 = [complex(0,(1000*math.sin(2*math.pi*x/16))) for x in range(0,16)]
ws2 = [complex(0,(1000*math.sin(2*math.pi*x/16)+10000*math.sin(6*math.pi*x/16)+15000*math.sin(10*math.pi*x/16))) for x in range(0,16)]
ws3 = [complex(0,(1000*math.sin(2*math.pi*x/8)+10000*math.sin(6*math.pi*x/8)+15000*math.sin(10*math.pi*x/8))) for x in range(0,8)]

class AudioTest(unittest.TestCase):


  def testDft1(self):
    self.assertEqual(list(map(lambda x:round(abs(x).real),dft(ws1))),[0,500,0,0,0,0,0,0,0,0,0,0,0,0,0,500] ,"dft falsch")

  def testDft2(self):
    self.assertEqual(list(map(lambda x:round(abs(x).real),dft(ws2))),[0,500,0,5000,0,7500,0,0,0,0,0,7500,0,5000,0,500] ,"dft falsch")

  def testDft3(self):
    self.assertEqual(list(map(lambda x:round(abs(x).real),dft(ws3))),[0,500,0,2500,0,2500,0,500] ,"dft falsch")

    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AudioTest)
    xmlrunner.XMLTestRunner(output=".").run(suite)
    
  
