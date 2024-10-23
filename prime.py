def is_prime_iterative(n):
    if n <= 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example:
print(is_prime_iterative(11))  # Output: True
print(is_prime_iterative(8))   # Output: False

# or
def prime_(n,x=None):
  if x is None:
    x=n-1
  if x<2:
    return True
  if n%x==0:
    return False
  return prime_(n,x-1)
print(prime_(3))
