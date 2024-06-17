def is_palindrome(i, n, s):
    if (i > n//2):
        return True

    if s[i] == s[n-i]: 
        return is_palindrome(i+1, n, s)
    return False
    
    

s = input()
n = len(s)
print(is_palindrome(0, n-1, s))