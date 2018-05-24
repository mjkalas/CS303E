'''
Assignment 1 - 2015
CS303E
Gives date of Easter Sunday given year using algorithm invented by Carl Friedrich Gauss
'''
import calendar

def main ():
    
    y = int(input("Enter year: "))
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    print("In", y, "Easter Sunday is on", p, calendar.month_name[n])
main ()
