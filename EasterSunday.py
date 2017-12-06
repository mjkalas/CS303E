#  File: EasterSunday.py

#  Description: This program computes the date of Easter Sunday given any year.

#  Student Name: Minal Kalas

#  Student UT EID: mjk863

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 09/08/15

#  Date Last Modified: 09/08/15

def main():
  #prompt the user to enter the year
  y = int (input ("Enter year: "))
  
  #perform computations to find the day
  a = y % 19
  b = y // 100
  c = y % 100
  d = b // 4
  e = b % 4
  g = (8*b+13) // 25
  h = (19*a+b-d-g+15) % 30
  j = c // 4
  k = c % 4
  m = (a+11*h) // 319
  r = (2*e+2*j-k-h+32) % 7
  n = (h-m+r+90) // 25
  p = (h-m+r+n+19) % 32
  
  #print the result
  month = ""
  if (n == 3):
    month = "March"
  if (n == 4):
    month = "April"
  print ("In", y, "Easter Sunday is on", p, month, end=".")
main()
