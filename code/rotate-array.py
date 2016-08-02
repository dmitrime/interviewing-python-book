def rotate_left(ar, n):
    if len(ar) > 1:
        n = n % len(ar)
        return ar[n:] + ar[:n]
    return ar

def rotate_right(ar, n):
    return rotate_left(ar, len(ar)-n)

def rotate(ar, n):
    if len(ar) > 1:
        n = n % len(ar)
        return ar[n:] + ar[:n]
    return ar

def rotate_left_manual(ar, n):
    n = n % len(ar)
    br = [ar[i] for i in range(n, len(ar))]
    for i in range(n):
        br.append(ar[i])
    return br


if __name__ == '__main__':
    #for i in range(5):
        #print rotate_left(range(1, 11), i)
        #print rotate_left_manual(range(1, 11), i)
        #print
    print rotate_left([1], 10)

    print rotate_left(range(1, 11), 2)
    print rotate_right(range(1, 11), 9)

    assert rotate_left([], 1) == []

    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 23) == \
        [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14) == \
        [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

    assert rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 23) == \
        [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

    assert rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -14) == \
        [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
