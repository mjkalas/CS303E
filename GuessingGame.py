def main ():
  a = []
  for i in range (1, 101):
    a.append(i)
  print ("Think of a number between 1 and 100 inclusive.")
  print ("And I will guess what it is in 7 tries or less.")
  print ()
  answer = input("Are you ready? (y/n):")
  while answer != "y" and answer != "n":
    answer = input("Are you ready? (y/n):")
  if answer == "y":
    count = 0
    lo = 0
    hi = len(a)-1
    while count < 7:
      mid = (lo + hi) // 2
      print ("Guess", count+1, ": The number you thought was", a[mid])
      guess  = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct:"))
      print ()
      count += 1
      if guess == 1:
        hi = mid -1
        if hi == -1:
          hi += 1
      elif guess == -1:
        lo = mid +1
      elif guess == 0:
        print ("Thank you for playing the Guessing Game.")
        return
      else:
        guess  = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: 1"))
    if count == 7:
      print ("Either you guessed a number out of range or you had an incorrect entry.")
  else:
    print ("Bye")
main()
