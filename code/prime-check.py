import math

def is_prime(X):
    sqrtX = int(math.sqrt(X)) + 1
    return all([X % n != 0 for n in range(2, sqrtX)])

def is_prime_basic(X):
    for n in range(2, X-1):
        if X % n == 0:
            return False
    return True

if __name__ == '__main__':
    assert is_prime(19) == True
    assert is_prime(33) == False

    #for i in range(2, 30):
    #    if is_prime(i):
    #        print "prime: %d" % i
