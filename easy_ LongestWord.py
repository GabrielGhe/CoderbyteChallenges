def LongestWord(sen):
  #only take whitespace and alphanumeric characters
  sen = "".join([c for c in sen if (c.isalpha() or c == " " or c.isdigit())])
  #split into words
  sen = sen.split()
  maxWord = ''
  maxLen = 0
  #find longest word
  for word in sen:
    if len(word) > maxLen:
      maxWord = word
      maxLen = len(word)
  return maxWord
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())           
