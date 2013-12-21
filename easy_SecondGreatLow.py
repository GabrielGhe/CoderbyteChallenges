"""
Finds the second greatest
and second lowest value in
an array
"""
def SecondGreatLow(arr):
  arr = list(set(arr))
  arr.sort()
  stri = "{0} {1}".format(arr[0], arr[0])
  if len(arr) == 2:
    stri = "{0} {1}".format(arr[0], arr[1])
  elif len(arr) > 2:
    stri = "{0} {1}".format(arr[1], arr[-2])
  return stri
    
print SecondGreatLow(raw_input())           
