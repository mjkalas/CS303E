#  File: CreditCard.py
#  Description: This program determines if a credit card number is valid.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 303E
#  Unique Number: 50475
#  Date Created: 10/24/15
#  Date Last Modified: 10/26/15

# This function checks if a credit card number is valid
def is_valid (cc_num):
  length = len(cc_num)
  sum = 0
  x = list(reversed(cc_num))
  for i in range (len(x)):
    if (i % 2 == 0):
      sum += x[i]
    else:
      if (i % 2 != 0):
        x[i] = (x[i]*2)
        sum += sum_digits(x[i])
  if (sum % 10 == 0):
    return True
  else:
    return False

# This function returns the type of credit card
def cc_type (cc_num):
  if cc_num[0] == 3 and cc_num[1] == 4:
    return ("American Express")
  if cc_num[0] == 3 and cc_num[1] == 7:
    return ("American Express")
  if cc_num[0] == 6 and cc_num[1] == 0 and cc_num[2] == 1 and cc_num[3] == 1:
    return ("Discover")
  if cc_num[0] == 6 and cc_num[1] == 4 and cc_num[2] == 4:
    return ("Discover")
  if cc_num[0] == 6 and cc_num[1] == 5:
    return ("Discover")
  if cc_num[0] == 5 and cc_num[1] == 0:
    return ("MasterCard")
  if cc_num[0] == 5 and cc_num[1] == 5:
    return ("MasterCard")
  if cc_num[0] == 4:
    return ("Visa")
  return ""

def sum_digits (n):
  sum_d = 0
  while (n > 0):
    sum_d = sum_d + n % 10
    n = n // 10
  return sum_d

def main():
    y = str (input ("Enter 15 or 16-digit credit card number: "))
    y = list(y)
    if (len(y) == 15) or (len(y) == 16):
      for i in range (len(y)):
        y[i] = int(y[i])
      validity = is_valid (y)
      if (validity == True):
        company = cc_type (y)
        print ("Valid", company, "credit card number")
      else:
        print ("Invalid credit card number")
    else:
      print ("\n"+"Not a 15 or 16-digit number")

main()
