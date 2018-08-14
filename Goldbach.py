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

def goldbach (num):
    output = str(num)
    i = 0
    while (i <= (num // 2 - 1)):
        i = i + 1
        if (is_prime(i) and is_prime (num - i)):
            output = output + " = " + str(i) + " + " + str(num - i)
    return output

def main ():
    lower = int(input("Please enter the lower limit: "))
    while ((lower < 4) or (lower % 2 != 0)):
        lower = int(input("Please enter the lower limit: "))
    upper = int(input("Please enter the upper limit: "))
    while ((upper < lower) or (upper % 2 != 0)):
        upper = int(input("Please enter the upper limit: "))

    evens = list(range(lower, upper + 1, 2))
    for num in evens:
        print (goldbach (num))
main()
