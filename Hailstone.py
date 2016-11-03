#  File: Hailstone.py
#  Description: This program finds the number in the given range with the longest cycle length.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 303E
#  Unique Number: 50475
#  Date Created: 09/17/15
#  Date Last Modified: 09/20/15


def main():
  # prompt the user to enter starting and ending numbers
  l = int (input ("Enter starting number of the range:"))
  h = int (input ("Enter ending number of the range:"))
  while ((l < 1) or (h < 1) or (l > h)):
      l = int (input ("Enter starting number of the range:"))
      h = int (input ("Enter ending number of the range:"))

  #define variables


  #run algorithm
  for n in range (l, h+1):
    max_num = 0
    max_length = 0
    num = n
    cycle_length = 0
    while (n > 1):
      if (n % 2 == 0):
        n = (n // 2)
        cycle_length += 1
      else:
        if (n % 2 == 1):
          n = (3 * n + 1)
          cycle_length += 1

  #get max cycle length
  if (cycle_length > max_length):
    max_length = cycle_length
    max_num = num

  # print results
  print ("The number", max_num, "has the longest cycle length of", str(max_length)+".")

main()
