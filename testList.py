from listUtils import *

print "Starting List testing"

assert list_product([1]) == 1
assert list_product([100]) == 100
assert list_product([1,2,3]) == 6
assert list_product([1,0,3]) == 0

list = ["1","2","3"]
list_roll_left(list, "4")
assert list == ["2","3","4"]
list = [3,2,1]
list_roll_right(list, 4)
assert list == [4,3,2]

print "List testing successful"
