"""
Find out if a series
follows a geometric or
arithmetic order
"""
def ArithGeoII(arr): 
  arr.reverse()
  geo = arr[0] / arr[1]
  ari = arr[0] - arr[1]
  geoB = ariB = True

  for idx,val in enumerate(arr[1:]):
    if ( arr[idx] - val ) != ari:
      ariB = False
    if ( arr[idx] / val ) != geo:
      geoB = False
      
  if ariB:
    return "Arithmetic"
  elif geoB:
    return "Geometric"
  else:
    return "-1"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeoII(raw_input())           
