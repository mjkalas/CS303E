def convert_fib_base(num):
	Fib_series = [1, 2]
	for i in range (0, num):
		Fib_series.append (Fib_series[i] + Fib_series[i+1])
	Fib_series.reverse()

	Fib_base = ""
	for i in Fib_series:                          
		if (num - i) >= 0:
		  Fib_base = Fib_base + "1"
		  num = num - i
		else:
		  Fib_base = Fib_base + "0"
	return (Fib_base)

def main ():
  import string
  num = int(input("Enter a number:"))
  while num < 0:
    num = int(input("Enter a number:"))
  Fibonacci_Base = convert_fib_base (num)
  Fibonacci_Base = Fibonacci_Base.lstrip ("0")
  print (num, "=", Fibonacci_Base, "(fib)")
main ()
