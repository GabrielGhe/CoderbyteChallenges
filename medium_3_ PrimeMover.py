############################
#  Find's the num'th prime #
############################
def PrimeMover(num):
  array = [2]
  current = 3
  ctr = 1
  while(ctr < num):
    is_prime = True
    #Try to mod by all the found primes up to now
    for prime in array:
      #current value can be divided by a prime
      if current % prime == 0:
        is_prime = False
    #Was the number a prime?
    if is_prime:
      array.append(current)
      ctr += 1
    #go to the next odd number
    current += 2
  return array[-1]
    

print PrimeMover(raw_input())           
