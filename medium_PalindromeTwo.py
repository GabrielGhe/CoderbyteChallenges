"""
Find out if a
string is a palindrome
"""
def PalindromeTwo(str): 
  str = str.lower()
  str = "".join([c for c in str if c.isalpha()])
  return "true" if str == str[::-1] else "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PalindromeTwo(raw_input())           
