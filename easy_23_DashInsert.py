def odd(ch):
  return ch in '13579'

##############################
# Inserts dashes between odd #
# digits                     #
##############################
def DashInsert(num):
  result = []
  prev = ' '
  for curr in str(num):
    if odd(prev) and odd(curr): 
      result.append('-')
    result.append(curr)
    prev = curr
  return ''.join(result)

print DashInsert(raw_input())           
