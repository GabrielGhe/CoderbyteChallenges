"""
Try to see if str2
can be made using characters
from str1
"""
def StringScramble(str1,str2): 
  for char in str2:
    x = str1.find(char)
    if x == -1:
      return "false"
    str1 = str1[:x] + str1[x + 1:]
  return "true"
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringScramble(raw_input())           
