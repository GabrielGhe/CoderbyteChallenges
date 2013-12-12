#Finds the longest word in a string
def LongestWord(sen): 
  
  #split string by white space
  words = sen.split()
  maxWord = ''
  maxLen = 0
  
  #go through each word
  for x in words:
    #first remove any non alphanumeric characters
    x = x.strip('!@#$%^&*()-=_+{}[];:,./<>?`~\|')
    if len(x) > maxLen:
      maxLen = len(x)
      maxWord = x
  
  #return longest word
  return maxWord
    

print LongestWord(raw_input())           
