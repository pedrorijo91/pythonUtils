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

list = [1,2,3,4,5,6]
assert delete_elems(list, []) == list
assert delete_elems(list, [3]) == [1,2,4,5,6]
assert delete_elems(list, [3,1,5]) == [2,4,6]
assert delete_elems(list, [7]) == [1,2,3,4,5,6]

print "List testing successful"
