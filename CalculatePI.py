import math
import random

def computePI (numThrows):
  in_points = 0  
  for i in range (numThrows):
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)
    if ((math.hypot (xPos, yPos)) < 1):
      in_points += 1
  PI = (in_points/numThrows) * 4
  return PI

def main ():
  nums = [100, 1000, 10000, 100000, 1000000, 10000000]
  for i in nums:
      output = computePI(i)
      diff = output - math.pi
      if diff < 0:
        sign = "-"
      else:
        sign = "+"
      print ("num = ", i, " "*(11-len(str(i))), "Calculated pi = ", format(output, ".6f")," "*4, "Difference = ", sign, format(abs(diff), ".6f"))
main ()
