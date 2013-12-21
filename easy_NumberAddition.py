"""
Traverse a string,
add up all the numbers
and return the final result

ex: '55blah 4' = 55 + 4 = 59
"""
def NumberAddition(str): 
  sum = 0
  temp = '0'
  for x in str:
    if x.isdigit():
      temp += x
    else:
      sum += int(temp)
      temp = '0'
  return sum + int(temp)
    
print NumberAddition(raw_input())           
