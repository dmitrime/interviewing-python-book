def to_binary(N):
    if N == 0:
        return '0'
    bits = ''
    while N > 0:
        bits += '1' if N & 1 else '0'
        N >>= 1
    return bits[::-1]

if __name__ == '__main__':
    print to_binary(328)
    print to_binary(16)
    print to_binary(0)
    assert to_binary(328) == '101001000'
    assert to_binary(16) == '10000'
    assert to_binary(0) == '0'
