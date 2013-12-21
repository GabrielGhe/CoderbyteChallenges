def vowel(str):
  return str in "aeiou"

"""
Turns characters into the
following characters in the
sequence and changes vowels
to uppercase
"""
def LetterChanges(str): 
  result = []
  for char in str:
    if char.isalpha():
      result.append(chr(ord(char) + 1))
    else:
      result.append(char)
  for idx in range(0, len(result)):
    if vowel(result[idx]):
      result[idx] = result[idx].upper()
  return "".join(result) 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())           
