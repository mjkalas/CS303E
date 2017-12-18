def partial_sum (a):
  par_sum = []
  y = 0
  for i in a:
    y += i
    par_sum.append (y)
  return par_sum

def sum_s1(b):
  x = 0
  for i in b:
    x += i
  return(x)

def checkISBN(isbn):
  list2 = []
  if len(isbn) != 10:
    return False

  for i in range (len(isbn)-1):
    if (isbn[i] == "x") or (isbn[i] == "X"):
      return False
    else:
      list2.append(int(isbn[i]))

  if (isbn[-1] == "x") or (isbn[-1] == "X"):
    list2.append(10)
  else:
    list2.append (int(isbn[-1]))

  s1 = partial_sum(list2)

  s2 = sum_s1 (s1)

  if (s2 % 11 == 0):
    return True
  else:
    return False


def main ():
  #open file for reading
  in_file = open("./isbn.txt", "r")

  # read lines in file
  for line in in_file.readlines():
    line = line.rstrip("\n")
    original = line
    line = line.replace ("-", "")
    line = list(line)

    if ((checkISBN(line)) == True):
      print (original, "valid")
    else:
      print (original, "invalid")


  in_file.close
main ()
