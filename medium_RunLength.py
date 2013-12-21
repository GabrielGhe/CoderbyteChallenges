"""
Determine the run length
of a string
ex: aaabbrerr > 3a2b1r1e2r
"""
def RunLength(string):
  val = string[0]
  count = 1
  ret = ""
  for char in string[1:]:
    if char != val:
      ret += str(count)
      ret += val
      val = char
      count = 1
    else:
      count += 1
  ret += str(count)
  ret += val
  return ret
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print RunLength(raw_input())           
