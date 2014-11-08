from fibUtils import *

print "Starting List testing"

assert nth_fib(1) == 1
assert nth_fib(2) == 1
assert nth_fib(3) == 2
assert nth_fib(5) == 5
assert nth_fib(10) == 55
assert nth_fib(20) == 6765

assert fib_len(2) == 7
assert fib_len(3) == 12
assert fib_len(4) == 17

print "List testing successful"
