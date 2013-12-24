import itertools

"""
Given a number,
using the digits in that number
find the next biggest number
"""
def PermutationStep(num): 
  arr = list(str(num))
  lis = set()
  
  for perm in itertools.permutations(arr, len(arr)):
    x = int("".join(list(perm)))
    if x > num:
      lis.add(x)
  
  lis = list(lis)
  lis.sort()
  
  if len(lis) > 0:
    return lis[0]
  return "-1"
    

print PermutationStep(raw_input())           
