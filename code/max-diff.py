def max_diff1(a):
    diff = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] - a[i] > diff:
                diff = a[j] - a[i]
    return diff

def max_diff2(a):
    minimum, diff = a[0], 0
    for i in range(1, len(a)):
        if a[i] - minimum > diff:
            diff = a[i] - minimum
        if a[i] < minimum:
            minimum = a[i]
    return diff

def max_diff3(a):
    maximum, diff = a[-1], 0
    for i in range(len(a)-2, -1, -1):
        if maximum - a[i] > diff:
            diff = maximum - a[i]
        if maximum < a[i]:
            maximum = a[i]
    return diff

if __name__ == '__main__':
    assert max_diff2([9, 3, 6, 8, 10, 4, 3]) == 7
    assert max_diff1(range(10+1)) == 10
    assert max_diff1(range(10, 0, -1)) == 0
