
def atoi(string):
    if string is None:
        return None
    # remove whispace on the left and right
    s = string.strip()
    # string was empty
    if len(s) == 0:
        return None
        
    # check for leading '-' or '+'
    neg = False
    if s[0] == '-':
        neg = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # loop over string as long as
    # element at i-th position is a digit
    i = 0
    while i < len(s) and s[i].isdigit():
        i += 1

    # there are non-digits left in the string
    if i < len(s) and s[i] != '.':
        return None

    # break string into integer and fractional part
    # i+1 skips the '.'
    s, t = s[:i], s[i+1:]
    
    # build the integer part by multiplying
    # digits with increasing powers of 10
    x, mul = 0, 1
    for j in reversed(range(len(s))):
        x += int(s[j]) * mul
        mul *= 10
        
    # when we have a fractional part...
    if len(t) > 0: 
        # build the fractional part by multiplying
        # digits with increasing powers of 0.1
        mul = 0.1
        for j in range(len(t)):
            # check for non-digits
            if not t[j].isdigit():
                return None
            x += int(t[j]) * mul
            mul *= 0.1

    # return either negative or positive number
    return x * -1 if neg else x


if __name__ == '__main__':
    import math

    assert atoi(None) == None
    assert atoi('') == None
    assert atoi('0') == 0
    assert atoi('-123') == -123
    assert atoi('+321') == 321
    assert atoi('1x') == None
    assert math.fabs(atoi('-456.1234') - -456.1234) <= 1e-10
    assert math.fabs(atoi('0.1234') - 0.1234) <= 1e-10
    assert atoi('-456.1234x') == None
