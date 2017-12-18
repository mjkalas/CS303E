# prints the product of diagonal going right to left
def prod_rl (b):
  prod = 1
  max_prod = 0
  for i in range (len(b[0])-3):
    for j in range (len(b[i])-3):
      prod = (b[i][j])*(b[i+1][j+1])*(b[i+2][j+2])*(b[i+3][j+3])
      if prod > max_prod:
        max_prod = prod
  return (max_prod)

# prints the product of diagonal going left to right
def prod_lr (b):
  prod = 1
  max_prod = 0
  for i in range (3, len(b)):
    for j in range (len(b[i])-3):
      prod = (b[i][j])*(b[i-1][j+1])*(b[i-2][j+2])*(b[i-3][j+3])
      if prod > max_prod:
        max_prod = prod
  return (max_prod)

# prints product of the columns in a 2-D list
def prod_cols (b):
  prod = 1
  max_prod = 0
  for i in range (len(b[0])-3):
    for j in range (len(b)):
      prod = (b[i][j])*(b[i+1][j])*(b[i+2][j])*(b[i+3][j])
      if prod > max_prod:
        max_prod = prod
  return (max_prod)

# prints the products of rows in a 2-D list
def prod_rows (b):
  prod = 1
  max_prod = 0
  for i in range (len(b)):
    for j in range (len(b[i])-3):
      prod = (b[i][j] * b[i][j+1])*(b[i][j+2]*(b[i][j+3]))
      if prod > max_prod:
        max_prod = prod
  return (max_prod)
    
def main():
  # open file for reading
  in_file = open ("./grid.txt", "r") 

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int (dim)

  # create a 2-D list
  grid = []

  # read data line by line
  for i in range (dim):
    line = in_file.readline()
    line = line.strip()

    # split the line
    nums = line.split()

    # convert into integers
    for j in range (dim):
      nums[j] = int (nums[j])

    # append nums to the 2-D list
    grid.append (nums)

  max_prod = 0

  # find the product of each row
  row = prod_rows (grid)
  if row > max_prod:
    max_prod = row
  # find the product of each column

  cols = prod_cols (grid)
  if cols > max_prod:
    max_prod = cols

  # find the diagonal going left to right
  lr = prod_lr (grid)
  if lr > max_prod:
    max_prod = lr

  # find the diagonal going right to left
  rl = prod_rl (grid)
  if rl > max_prod:
    max_prod = rl

  print ("The greatest product is", max_prod)

  # close file
  in_file.close()

main()
