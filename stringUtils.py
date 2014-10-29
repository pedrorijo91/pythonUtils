def is_palindrome(s):
        lst = list(s)

        for i in range(len(lst)/2):
                if lst[i] <> lst[len(lst)-1-i]:
                        return False

        return True
