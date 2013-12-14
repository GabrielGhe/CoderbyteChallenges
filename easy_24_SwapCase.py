def SwapCase(str): 
  result = ""
  for x in str:
    if x.isupper():
      result += x.lower()
    else:
      result += x.upper()
  return result
    
print SwapCase(raw_input())  
