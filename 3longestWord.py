#Finds the longest word in a string

#1. Split the string by space using .split()
#2. using max function to find the biggest using the length as the criteria
def LongestWord(sen): 
    return max(sen.split(), key=len)
     
print LongestWord(raw_input())
