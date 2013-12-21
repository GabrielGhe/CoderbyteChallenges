"""
Find the word with
the most repeating
characters
"""
def LetterCountI(str): 
  dict = {}
  maxWord = ''
  repeat = 0
  
  #Go through every word
  for word in str.split():
    dict.clear()
    #go through every letter in the word
    for letter in word:
      #place them in the dict or increment
      if dict.has_key(letter):
        dict[letter] += 1
      else:
        dict[letter] = 1
    #check if it's better than current best
    if max(dict.values()) > repeat:
      repeat = max(dict.values())
      maxWord = word
      
  return maxWord if repeat > 1 else "-1" 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCountI(raw_input())           
