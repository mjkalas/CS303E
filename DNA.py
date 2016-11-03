#  File: DNA.py

#  Description:

#  Student Name: Minal Kalas

#  Student UT EID: mjk863

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 10/13/15

#  Date Last Modified: 10/14/15

def main():
  # open file for reading
  in_file =  open ("./dna.txt", "r")

  # read number of pairs
  num_pairs = in_file.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  # read each pair of dna strands
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()

    # remove white space from either end
    st1 = st1.strip()
    st2 = st2.strip()

    # make both strands upper case
    st1 = st1.upper()
    st2 = st2.upper()

    # order strands by size
    if (len(st1) > len(st2)):
      dna1 = st1
      dna2 = st2
    else:
      dna1 = st2
      dna2 = st1

    # get all substrings of dna2
    wnd = len (dna2)
    a = []
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len (dna2)):
        sub_strand = dna2[start_idx: start_idx + wnd]
        if sub_strand in dna1:
          if (len(sub_strand)) >= len(a):
            a = sub_strand
            if (len(a) > 0):
              print ("Pair", str(i+1)+":", a)
  
        # move starting place by 1
        start_idx += 1

  # decrease window size
      wnd = wnd - 1
  

    if (len(a) <=0):
      print ("Pair", str(i+1)+":", "No Common Sequence Found")
   
  # close file
  in_file.close()

main()