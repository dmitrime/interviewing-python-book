def generate_parens2(n):
    strings = set()
    def _gen(s, opn, cls):
        if opn == n and cls == n:
            strings.add(s)
        if opn < n:
            _gen(s + '(', opn+1, cls)
        if cls < opn:
            _gen(s + ')', opn, cls+1)

    _gen('', 0, 0)
    return strings

def generate_parens1(n):
    ''' Relies on the set data structure '''
    strings = set()
    if n == 0:
        strings.add("")
    else:
        strings_prev = generate_parens2(n-1)
        for s in strings_prev:
            strings.add('()' + s)
            strings.add('(' + s + ')')
            strings.add(s + '()')
    return strings

if __name__ == '__main__':
    assert generate_parens1(0) == set([''])
    assert generate_parens1(1) == set(['()'])
    assert generate_parens1(3) == set(['()()()', '((()))', '()(())', '(())()', '(()())'])
    #assert generate_parens2(3) == set(['()()()', '((()))', '()(())', '(())()', '(()())'])
    print generate_parens2(4)
    print generate_parens1(3)
    print generate_parens2(0)
