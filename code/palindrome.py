def is_palindrome1(s):
    return s == s[::-1]

def is_palindrome2(s):
    l = len(s)
    return all([s[i] == s[l-i-1] for i in range(l / 2)])

def is_palindrome3(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    #print is_palindrome1('abcdcba')
    #print is_palindrome1('abcdcbax')

    print is_palindrome2('abcdcba')
    print is_palindrome2('abcdcbax')

    #print is_palindrome3('abcdcba')
    #print is_palindrome3('abcdcbax')


    assert is_palindrome1('aBcDxDcBa') == True
    assert is_palindrome1('aBcDxDcB') == False
