def fact(n):
    #base case
    if n==0:
        return 1
    return n*fact((n-1))
	
fact(5) -->120