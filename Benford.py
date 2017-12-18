# Outline of Benford.py
def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['0'] = 0
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0
  pop_freq

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    pop_num = pop_data[-1]

    # process the data
    pop_freq[pop_num[0]] += 1
    pop_freq['0'] += 1

  # close the file
  in_file.close()

  # write out the result
  print ("Digit   Count   %")
  print ("1      ", pop_freq['1'],"  ", round(((pop_freq['1']/pop_freq['0'])*100), 1))
  print ("2      ", pop_freq['2'],"  ", round(((pop_freq['2']/pop_freq['0'])*100), 1))
  print ("3      ", pop_freq['3'],"  ", round(((pop_freq['3']/pop_freq['0'])*100), 1))
  print ("4      ", pop_freq['4'],"  ", round(((pop_freq['4']/pop_freq['0'])*100), 1))
  print ("5      ", pop_freq['5'],"  ", round(((pop_freq['5']/pop_freq['0'])*100), 1))
  print ("6      ", pop_freq['6'],"  ", round(((pop_freq['6']/pop_freq['0'])*100), 1))
  print ("7      ", pop_freq['7'],"  ", round(((pop_freq['7']/pop_freq['0'])*100), 1))
  print ("8      ", pop_freq['8'],"  ", round(((pop_freq['8']/pop_freq['0'])*100), 1))
  print ("9      ", pop_freq['9'],"   ", round(((pop_freq['9']/pop_freq['0'])*100), 1))
  
main()
