#  File: Goldbach.py
#  Description: This program verifies Goldbach's Conjecture for a user-inputted range of numbers.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 303E
#  Unique Number:50475
#  Date Created: 09/21/15
#  Date Last Modified: 09/24/15

# check if a number is prime
def is_prime (n):
  limit = int (n ** 0.5) + 1
  divisor = 2
  if (n == 1):
	  return False
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor = divisor + 1
  return True

# chcck if number is even
def even(num):
	if (num % 2 == 0):
		return True
	else:
		return False

#make answers print on same line
def same_lines (n):
	str_same = str(n)
	i = 0
	while (i <=(n/2-1)):
		i = i+1
		if (is_prime(i) and is_prime(n-i)):
			str_same = str_same+" = "+str(i)+" + "+str(n-i)
	return (str_same)

def main ():
	# Prompt user to enter range
	lower = eval(input("Enter the lower limit:"))
	upper = eval(input("Enter the upper limit:"))
	while lower < 4:
		print ("Lower limit must be greater than or equal to 4.")
		lower = eval(input("Enter the lower limit:"))
		upper = eval(input("Enter the upper limit:"))
	while even(lower) is False or even(upper) is False:
		print ("Lower limit and upper limit must be even numbers.")
		lower = eval(input("Enter the lower limit:"))
		upper = eval(input("Enter the upper limit:"))
	while (lower > upper):
		print ("Upper limit must be greater than lower limit.")
		lower = eval(input("Enter the lower limit:"))
		upper = eval(input("Enter the upper limit:"))

	#print output
	for i in range (lower, upper+1, 2):
		print (same_lines(i))
main ()
