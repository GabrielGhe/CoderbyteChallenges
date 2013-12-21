def ExOh(str): 
  dict = {"x":0, "o":0}
  for x in str:
    dict[x.lower()] += 1
  return "true" if dict['x'] == dict['o'] else "false"
    
print ExOh(raw_input())           
