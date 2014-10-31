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

assert combinations(3,3) == 1 
assert combinations(2,2) == 1 
assert combinations(100,100) == 1 
assert combinations(3,1) == 3 
assert combinations(5,1) == 5
assert combinations(17,1) == 17 
assert combinations(5,2) == 10 
assert combinations(12,4) == 495

assert number_3d_to_text(1) == "one"
assert number_3d_to_text(10) == "ten" 
assert number_3d_to_text(20) == "twenty"
assert number_3d_to_text(90) == "ninety" 
assert number_3d_to_text(99) == "ninety nine" 
assert number_3d_to_text(155) == "one hundred and fifty five" 
assert number_3d_to_text(342) == "three hundred and forty two" 
assert number_3d_to_text(115) == "one hundred and fifteen"
assert number_3d_to_text(836) == "eight hundred and thirty six"
assert number_3d_to_text(527) == "five hundred and twenty seven" 
assert number_3d_to_text(901) == "nine hundred and one" 
assert number_3d_to_text(101) == "one hundred and one" 
assert number_3d_to_text(999) == "nine hundred and ninety nine"
assert number_3d_to_text(100) == "one hundred" 

assert number_to_text(1000) == "one thousand" 
assert number_to_text(1) == "one"
assert number_to_text(10) == "ten" 
assert number_to_text(20) == "twenty"
assert number_to_text(90) == "ninety" 
assert number_to_text(99) == "ninety nine" 
assert number_to_text(155) == "one hundred and fifty five" 
assert number_to_text(342) == "three hundred and forty two" 
assert number_to_text(115) == "one hundred and fifteen"
assert number_to_text(836) == "eight hundred and thirty six"
assert number_to_text(527) == "five hundred and twenty seven" 
assert number_to_text(901) == "nine hundred and one" 
assert number_to_text(101) == "one hundred and one" 
assert number_to_text(999) == "nine hundred and ninety nine"
assert number_to_text(1001) == "one thousand one"
assert number_to_text(1010) == "one thousand ten" 
assert number_to_text(1020) == "one thousand twenty"
assert number_to_text(3090) == "three thousand ninety" 
assert number_to_text(10099) == "ten thousand ninety nine" 
assert number_to_text(155155) == "one hundred and fifty five thousand one hundred and fifty five" 

print "Number testing successful"
