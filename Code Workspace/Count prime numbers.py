def primeList(number):
  #storage
  primes = [2]
  #driver
  for num in range(3,number+1,2): 
    #engine
    flag = True
    for i in range(2,num//2 + 1):
      if num%i ==0:
        flag = False
        break
    if flag:
      primes.append(num)
  return primes

print(primeList(25))