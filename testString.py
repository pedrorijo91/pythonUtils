from stringUtils import *

print "Starting String testing"

assert is_palindrome("aa") == True
assert is_palindrome("aba") == True
assert is_palindrome("abbcccdcccbba") == True
assert is_palindrome("123321") == True
assert is_palindrome("ab") == False
assert is_palindrome("aaacbbaaa") == False
assert is_palindrome("123323") == False
assert is_palindrome("13195") == False
assert is_palindrome("0") == True
assert is_palindrome("999") == True
assert is_palindrome("1221") == True

print "String testing successful"
