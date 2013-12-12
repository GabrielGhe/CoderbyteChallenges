#Gets the factorial of a number
def FirstFactorial(num): 
  result = 1
  for x in range(1, num + 1):
    result *= x
  return result
    
print FirstFactorial(raw_input())  
