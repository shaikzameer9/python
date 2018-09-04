#def isPalindrome(s):
    #if len(s) <= 1:
        #return True
    #return s[0] == s[-1] and isPalindrome(s[1:-1])

#After running the code type isPalindrome([1,2,3,4,5,4,3,2,1]) and hit enter.
#Refer https://stackoverflow.com/questions/30340208/recursively-checking-if-a-list-is-a-palindrome-in-python
def is_palindrome(s, t='both'):
    # only odd sequences can be palindromes
    if t=='odd':
        if len(s)%2 == 0:
            return False
        else:
            return s == s[::-1]

    # only even sequences can be palindromes
    elif t=='even':
        if len(s)%2:
            return False
        else:
            return s == s[::-1]

    # both even or odd sequences can be palindromes
    else:
        return s == s[::-1]