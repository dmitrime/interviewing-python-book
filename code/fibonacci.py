def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def fib_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Still exceeds max rec depth for large N!!!
# RuntimeError: maximum recursion depth exceeded
def fib_memo(n):
    memo = dict()
    def _fib(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        else:
            if n not in memo:
                memo[n] = _fib(n-1) + _fib(n-2)
            return memo[n]
    return _fib(n)


if __name__ == '__main__':
    for i in range(31):
        print fib_iterative(i),
    print
    for i in range(31):
        print fib_memo(i),
    print
    #for i in range(31):
        #print fib_recursive(i),

    assert fib_recursive(0) == 0
    assert fib_recursive(1) == 1
    assert fib_recursive(6) == 8
    assert fib_recursive(30) == 832040

    assert fib_memo(0) == 0
    assert fib_memo(1) == 1
    assert fib_memo(30) == 832040
    assert fib_memo(500) == 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125

    assert fib_iterative(0) == 0
    assert fib_iterative(1) == 1
    assert fib_iterative(6) == 8
    assert fib_iterative(30) == 832040
    assert fib_iterative(1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
