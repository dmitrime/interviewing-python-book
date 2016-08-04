def max_diff1(a):
    diff = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] - a[i] > diff:
                diff = a[j] - a[i]
    return diff

def max_diff2(a):
    diff = 0
    if len(a) >= 2:
        minimum = a[0]
        for elem in a:
            minimum = min(minimum, elem)
            diff = max(diff, elem-minimum)
    return diff

def max_diff3(a):
    diff = 0
    if len(a) >= 2:
        maximum = a[-1]
        for elem in reversed(a):
            maximum = max(maximum, elem)
            diff = max(diff, maximum-elem)
    return diff

if __name__ == '__main__':
    assert max_diff1([]) == 0
    assert max_diff1([1]) == 0
    assert max_diff1([9, 3, 6, 8, 10, 4, 3]) == 7
    assert max_diff1(range(10+1)) == 10
    assert max_diff1(range(10, 0, -1)) == 0

    assert max_diff2([]) == 0
    assert max_diff2([1]) == 0
    assert max_diff2([9, 3, 6, 8, 10, 4, 3]) == 7
    assert max_diff2(range(10+1)) == 10
    assert max_diff2(range(10, 0, -1)) == 0

    assert max_diff3([]) == 0
    assert max_diff3([1]) == 0
    assert max_diff3([9, 3, 6, 8, 10, 4, 3]) == 7
    assert max_diff3(range(10+1)) == 10
    assert max_diff3(range(10, 0, -1)) == 0

