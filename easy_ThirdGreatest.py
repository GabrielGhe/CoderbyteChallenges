"""
Return the 3rd longest
string in an array of
strings
"""
def ThirdGreatest(strArr):
  #have to reverse because timsort is stable
  strArr = sorted(strArr, key = len, reverse = True)
  return strArr[2]
    
print ThirdGreatest(raw_input())           
