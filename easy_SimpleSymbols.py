"""
Takes a string and
returns True if every 
letter is between 2 +'s
"""
def SimpleSymbols(str):
  ret = True
  for idx, val in enumerate(str[1:-1]):
    #if alpha
    if val.isalpha():
      #check if chars on each side are +s
      if ( str[idx] != "+" ) or (str[idx + 2] != "+"):
        ret = False
        break
  return "true" if ret else "false"
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input())           
