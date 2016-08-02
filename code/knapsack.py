# Exponential time-complexity
def knapsack_rec(values, weights, total):
    def _knapsack(n, cur_v, cur_w):
        if n == len(values) or cur_w == 0:
            return cur_v
        v, w = values[n], weights[n]
        notTake = _knapsack(n+1, cur_v, cur_w)
        if cur_w-w >= 0:
            take = _knapsack(n+1, cur_v+v, cur_w-w)
            return max(take, notTake)
        else:
            return notTake

    return _knapsack(0, 0, total)

# Memoization. Polinomial time-complexity.
def knapsack_tab(values, weights, total):
    table = dict()
    def _knapsack(n, cur_v, cur_w):
        if n == len(values) or cur_w == 0:
            return cur_v
        if (n,cur_w) in table:
            return table[(n,cur_w)]
        v, w = values[n], weights[n]
        table[(n,cur_w)] = _knapsack(n+1, cur_v, cur_w)
        if cur_w-w >= 0:
            table[(n,cur_w)] = max(_knapsack(n+1, cur_v+v, cur_w-w),
                                   table[(n,cur_w)])
        return table[(n,cur_w)]

    return _knapsack(0, 0, total)

# 2-dimentional table. Polynomial time-complexity.
def knapsack_2d(values, weights, total):
    N = len(values)
    table = [[0]*(total+1) for _ in range(N+1)]

    for n in range(1, N+1):
        v, w = values[n-1], weights[n-1]
        for cur_w in range(total+1):
            if cur_w-w >= 0:
                table[n][cur_w] = max(table[n-1][cur_w-w] + v,
                                      table[n-1][cur_w])
    return table[N][total]


# 1-dimentional table. Polynomial time-complexity.
def knapsack_1d(values, weights, total):
    table = [0]*(total+1)
    for v,w in zip(values, weights):
        for cur_w in range(total, -1, -1):
            if cur_w-w >= 0:
                table[cur_w] = max(table[cur_w],
                                   table[cur_w-w]+v)
    return table[total]

if __name__ == '__main__':
    assert knapsack_rec([3, 5, 6], [1, 2, 3], 5) == 11
    assert knapsack_rec([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10) == 10
    assert knapsack_rec([1, 9], [9, 1], 9) == 9
    assert knapsack_rec([], [], 10) == 0
    assert knapsack_rec([1], [1], 0) == 0

    assert knapsack_tab([3, 5, 6], [1, 2, 3], 5) == 11
    assert knapsack_tab([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10) == 10
    assert knapsack_tab([1, 9], [9, 1], 9) == 9
    assert knapsack_tab([], [], 10) == 0
    assert knapsack_tab([1], [1], 0) == 0
    #assert knapsack_tab(range(995), range(995), 995) == 995

    assert knapsack_2d([3, 5, 6], [1, 2, 3], 5)
    assert knapsack_2d([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10) == 10
    assert knapsack_2d([1, 9], [9, 1], 9) == 9
    assert knapsack_2d([], [], 10) == 0
    assert knapsack_2d([1], [1], 0) == 0
    #assert knapsack_2d(range(5000), range(5000), 5000) == 5000

    assert knapsack_1d([3, 5, 6], [1, 2, 3], 5)
    assert knapsack_1d([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10) == 10
    assert knapsack_1d([1, 9], [9, 1], 9) == 9
    assert knapsack_1d([], [], 10) == 0
    assert knapsack_1d([1], [1], 0) == 0
    #assert knapsack_1d(range(5000), range(5000), 5000) == 5000
