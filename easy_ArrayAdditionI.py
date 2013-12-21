import itertools

#################################################
# This function will see if there is any        #
# possible combination of the numbers in        #
# the array that will give the largest number   #
#################################################
def ArrayAdditionI(arr):
  
  #sort, remove last element
  result = "false"
  arr.sort()
  large = arr[-1]
  arr = arr[:-1]
  
  #go through every combination and see if sum = large
  for x in range(2,len(arr) + 1):
    for comb in itertools.combinations(arr,x):
      if large == sum(comb):
        result = "true"
        break
  return result
    
print ArrayAdditionI(raw_input())      
