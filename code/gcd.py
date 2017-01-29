def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        print a, b
    return a

if __name__ == '__main__':
    assert gcd(40, 28) == 4
    assert gcd(14, 28) == 14
    assert gcd(1, 5) == 1
    assert gcd(5, 1) == 1
