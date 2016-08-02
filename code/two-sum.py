def two_sum(numbers, target):
    d = {target-n: i for i, n in enumerate(numbers)}
    for i, n in enumerate(numbers):
        if n in d and d[n] != i:
            return i, d[n]
    return -1, -1

def two_sum_basic(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j
    return -1, -1

if __name__ == '__main__':
    assert two_sum(numbers=[3, 2, 4, 7],
                   target=6) == \
        (1, 2)

    assert two_sum(numbers=[3, 2, 4, 7],
                   target=1) == \
        (-1, -1)

    assert two_sum_basic(numbers=[3, 2, 4, 7],
                   target=6) == \
        (1, 2)

    assert two_sum_basic(numbers=[3, 2, 4, 7],
                   target=1) == \
        (-1, -1)
