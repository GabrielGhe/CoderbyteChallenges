###################################
# Finds if num is a prime number  #
###################################
def PrimeTime(num):
  #1 is not a prime
  if num == 1:
    return "false"
  
  #it should only go up to it's sqrt
  limit = num**.5
  
  #from 2 to limit
  for x in range(2, int(limit) + 1):
    if num % x == 0:
      return "false"
  return "true" 
    

print PrimeTime(raw_input())    
