"""
Returns true if there are
exactly 3 characters in the
string seperating characters
a and b
"""
def ABCheck(str): 
  for x in range(len(str) - 4):
    if (str[x] == 'a' and str[x + 4] == 'b') or (str[x] == 'b' and str[x + 4] == 'a'):
      return "true"
  return "false" 
print ABCheck(raw_input()) 
