'''
Assignment 2
CS303E
Gives the day given a date
'''

import calendar

def day ():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    year = int(input("Enter year: "))
    while (year < 1900) or (year > 2100):
        year = int(input("Enter year: "))
    
    month = int(input("Enter month: "))
    while (month < 1) or (month > 12):
        month = int(input("Enter month: "))
    
    day = int(input("Enter day: "))
    if month == 2:
        if (calendar.isleap(year)):
            while (day < 1) or (day > 29):
                day = int(input("Enter day: "))
        else:
            while (day < 1) or (day > 28):
                day = int(input("Enter day: "))
    else:
         while (day < 1) or (day > 31):
            day = int(input("Enter day: "))

    index = calendar.weekday(year, month, day)
    print ("The day is " + days[index])

def main ():
    day ()
main ()
