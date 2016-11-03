#  File: Books.py
#  Description: Compares word frequency and variances within two given texts.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 303E
#  Unique Number: 50475
#  Date Created: 11/28/15
#  Date Last Modified: 11/30/15

# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
  word_list = open('./words.txt','r')
  word_dict = set()
  i = 0
  for line in word_list:
    word_dict.add(line.rstrip('\n'))
  word_list.close()
  return word_dict

# Removes punctuation marks from a string
def rem_punc(st):
  if len(st) == 0:
    return st
  if st[0].isalpha():
    if st[-1].isalpha():
      return st
    return rem_punc(st[:-1])
  return rem_punc(st[1:])

def parseString (st):
  Lst = []
  for word in st.replace('-',' ').split():
    if not word.isalpha():
      word = rem_punc(word).replace("'s",'')
    if word:
      Lst.append(word)
  return Lst

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  #open file
  f = open(file, 'r')
  words = {}
  for line in f:
    Lst = parseString(line.rstrip('\n'))
    for word in Lst:
      try:
        words[word] += 1
      except:
        words[word] = 1
    a = line

  #check for lower case version of upper case words
  upperWords = {}
  removedWords = set()
  for word in words:
    if word[0].isupper():
      upperWords[word] = words[word]
  for word in upperWords:
    if word.lower() in words:
      words[word.lower()] += upperWords[word]
    elif word.lower() in word_dict:
      words[word.lower()] = upperWords[word]
    else:
      removedWords.add(word) 
    del words[word]

  #close file
  f.close()
  return words

# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
  total_words_1 = 0
  word_count_1 = 0
  for word in freq1:
    total_words_1 += freq1[word]
    word_count_1 += 1
  total_words_2 = 0
  word_count_2 = 0
  for word in freq2:
    total_words_2 += freq2[word]
    word_count_2 += 1
  set1 = set(freq1)
  set2 = set(freq2)
  diff1 = set1 - set2
  diff2 = set2 - set1
  count1 = 0
  for x in diff1:
    count1 += freq1[x]
  count2 = 0
  for x in diff2:
    count2 += freq2[x]
  
  #Print results
  print()
  print(author1)
  print('Total distinct words =', word_count_1)
  print('Total words (including duplicates) =', total_words_1)
  print('Ratio (% of total distinct words to total words) =', \
        word_count_1/total_words_1*100, end = '\n\n')
  print(author2)
  print('Total distinct words =', word_count_2)
  print('Total words (including duplicates) =', total_words_2)
  print('Ratio (% of total distinct words to total words =', \
        word_count_2/total_words_2*100, end = '\n\n')
  print('%s used %d words that %s did not use.' %(author1, len(diff1), author2))
  print('Relative frequency of words used by %s not in common with %s =' \
        %(author1, author2), count1/total_words_1*100, end = '\n\n')
  print('%s used %d words that %s did not use.' %(author2, len(diff2), author1))
  print('Relative frequency of words used by %s not in common with %s =' \
        %(author2, author1), count2/total_words_2*100, end = '\n\n')

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
