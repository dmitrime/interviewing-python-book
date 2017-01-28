def three_sum_basic(numbers, target):
    N = len(numbers)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    return (i, j, k)
    return (-1, -1, -1)

def three_sum(numbers, target):
    numbers = sorted(list(numbers))
    for i in range(len(numbers) - 2):
        j = i+1
        k = len(numbers)-1
        while j < k:
            s = numbers[i] + numbers[j] + numbers[k]
            if s < target:
                j += 1
            elif s > target:
                k -= 1
            else:
                return (i, j, k)
    return (-1, -1, -1)


if __name__ == '__main__':
    assert three_sum_basic([-1, 1, 0], 0) == (0, 1, 2)
    assert three_sum_basic([-1, 1, 1], 0) == (-1, -1, -1)
    assert three_sum_basic([1, 2, 3, 4, 5, 6, 7, 8], 9) == (0, 1, 5)
    assert three_sum_basic([1, 2, 3, 4, 5, 6, 7, 8], 22) == (-1, -1, -1)

    assert three_sum([-1, 1, 0], 0) == (0, 1, 2)
    assert three_sum([-1, 1, 1], 0) == (-1, -1, -1)
    assert three_sum([1, 2, 3, 4, 5, 6, 7, 8], 9) == (0, 1, 5)
    assert three_sum([1, 2, 3, 4, 5, 6, 7, 8], 22) == (-1, -1, -1)
