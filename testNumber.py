from numberUtils import *

print "Starting Number testing"

assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(5) == True
assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(13) == True
assert is_prime(4) == False
assert is_prime(6) == False
assert is_prime(8) == False
assert is_prime(9) == False
assert is_prime(10) == False
assert is_prime(12) == False

assert divisors(1) == [1]
assert divisors(3) == [1, 3]
assert divisors(6) == [1, 2, 3, 6]
assert divisors(10) == [1, 2, 5, 10]
assert divisors(15) == [1, 3, 5, 15]
assert divisors(21) == [1, 3, 7, 21]
assert divisors(28) == [1, 2, 4, 7, 14, 28]

print "Number testing successful"
