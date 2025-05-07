from math import sqrt, floor
def is_prime(num):
  """
  Write a function, is_prime, that takes in a number as an argument. 
  The function should return a boolean indicating whether or not the given number is prime.

  A prime number is a number that is only divisible by two distinct numbers: 1 and itself.
  
  For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.
  
  Assumption: the input number is a positive integer.
  """
  if num < 2:
    return False

  for divisor in range(2, floor(sqrt(num)) + 1): # Factors alway come on pair and 
                                                 # sqrt will give the maximum pair without any duplicate
    if num % divisor == 0:
      return False
  return True

# Time Complexity -> O(sqrt(n))
# Spce complexity -> O(1)

print(f"1 -> {is_prime(1)}") # -> False
print(f"2 -> {is_prime(2)}") # -> True
print(f"3 -> {is_prime(3)}") # -> True
print(f"4 -> {is_prime(4)}") # -> False
print(f"5 -> {is_prime(5)}") # -> True
print(f"6 -> {is_prime(6)}") # -> False
print(f"7 -> {is_prime(7)}") # -> True
print(f"8 -> {is_prime(8)}") # -> False
print(f"25 -> {is_prime(25)}") # -> False
print(f"31 -> {is_prime(31)}") # -> True
print(f"2017 -> {is_prime(2017)}") # -> True
print(f"2048 -> {is_prime(2048)}") # -> False
print(f"713 -> {is_prime(713)}") # -> False