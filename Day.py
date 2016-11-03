#  File: Day.py
#  Description: This  program calculates the day of the week of any given date.
#  Student Name: Minal Kals
#  Student UT EID: mjk863
#  Course Name: CS 303E
#  Unique Number: 50475
#  Date Created: 09/15/15
#  Date Last Modified: 09/16/15

def main():
  # prompt the user to enter year
  year = int (input ("Enter year: "))
  while ((year < 1900) or (year > 2100)):
    year = int (input ("Enter year: "))

  # check if year is leap
  is_leap = (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))

  # prompt the user to enter month
  mon = int (input ("Enter month: "))
  while ((mon < 1) or (mon > 12)):
    mon = int (input ("Enter month: "))

  # prompt the user to enter day
  day = int (input ("Enter day: "))
  while ((day < 1) or (day > 31)):
    day = int (input ("Enter day: "))
  while (((mon == 1) or (mon == 3) or (mon == 5) or (mon == 7) or (mon == 8) or (mon == 10) or (mon == 12)) and (day > 31)):
    day = int (input ("Enter day: "))
  while (((mon == 4) or (mon == 6) or (mon == 9) or (mon == 11)) and (day > 30)):
    day = int (input ("Enter day: "))
  while ((mon == 2) and not is_leap and (day > 28)):
    day = int (input ("Enter day: "))
  while ((mon == 2) and is_leap and (day > 29)):
    day = int (input ("Enter day: "))

  # adjusting year for algorithm
  if (mon < 3):
    year = (year-1)

  # define variables
  if (mon >= 3):
    a = (mon - 2)
  if (mon < 3):
    a = (mon + 10)

  # day of month
  b = day    

  # year within the century
  c = (year % 100)

  #calculate century adjustment for algorithm
  d = year//100

  #Zeller's Algorithm
  w = (13 * a - 1 ) // 5
  x = c // 4
  y = d // 4
  z = (w + x + y + b + c - (2 * d))
  r = z % 7
  r = ((r + 7) % 7)

  #print the day of the week
  if (r==0):
    print ("The day is Sunday.")
  elif (r==1):
    print ("The day is Monday.")
  elif (r==2):
    print ("The day is Tuesday.")
  elif (r==3):
    print ("The day is Wednesday.")
  elif (r==4):
    print ("The day is Thursday.")
  elif (r==5):
    print ("The day is Friday.")
  else:
    if (r==6):
      print ("The day is Saturday.")
main()