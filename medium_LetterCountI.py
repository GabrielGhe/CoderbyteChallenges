"""
Find word with most
occuring letters
"""
def LetterCountI(str): 
  dict = {}
  maxWord = ''
  repeat = 0
  for word in str.split():
    dict.clear()
    for letter in word:
      if dict.has_key(letter):
        dict[letter] += 1
      else:
        dict[letter] = 1
    if max(dict.values()) > repeat:
      repeat = max(dict.values())
      maxWord = word
  return maxWord if repeat > 1 else "-1" 
    
print LetterCountI(raw_input())           
