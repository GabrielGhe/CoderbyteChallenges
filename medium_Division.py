"""
returns the greatest
common divisor for both
numbers
"""
def Division(num1,num2):
  if num1 == num2:
    return num1
  x = max(num1,num2)
  y = min(num1,num2)
  return Division(x - y, y) 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print Division(raw_input())           
