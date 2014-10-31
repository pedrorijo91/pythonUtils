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

assert remove_whitespace("") == ""
assert remove_whitespace("abc") == "abc"
assert remove_whitespace(" abc") == "abc"
assert remove_whitespace(" abc ") == "abc"
assert remove_whitespace(" ab c ") == "abc"
assert remove_whitespace(" ab	cd ") == "abcd"
assert remove_whitespace(" ab\tcd ") == "abcd"

print "String testing successful"
