def fib_rec(n):
  # Base Case
  if n == 0 or n == 1:
    return n
  # Recursion
  else:
    return fib_rec(n-2) + fib_rec(n-1)

print(fib_rec(6))
