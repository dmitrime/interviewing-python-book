def ways_coin_change(coins, amount):
    # table to remember number of ways to make up smaller amounts
    # waystable[0] is 1 since there's only one way to make up zero amount.
    waystable = [1] + [0]*amount
    for coin in coins:
        # from smaller to larger amounts
        for cur_amount in range(amount+1):
            if coin <= cur_amount:
                # add ways to make smaller amount
                waystable[cur_amount] += waystable[cur_amount - coin]
    return waystable[amount]

def ways_limit_coin_change(coins, amount):
    waystable = [1] + [0]*amount
    for coin in coins:
        # from larger to smaller
        for cur_amount in range(amount, -1, -1):
            if coin <= cur_amount:
                waystable[cur_amount] += waystable[cur_amount - coin]
    return waystable[amount]


if __name__ == '__main__':
    #print min_coin_change([1,5,10,25], 63)
    #for i in range(26):
        #print i, ways_coin_change([5,10,25], i)
    #for i in range(26):
        #print i, ways_limit_coin_change([1,5,5,10,25], i)

    assert ways_coin_change([], 25) == 0
    assert ways_coin_change([1,5], 0) == 1
    assert ways_coin_change([1,5,10,25], 25) == 13
    assert ways_coin_change([1,5,10,25], 37) == 24

    assert ways_limit_coin_change([], 25) == 0
    assert ways_limit_coin_change([1,5], 0) == 1
    assert ways_limit_coin_change([1,5,10,25], 25) == 1
    assert ways_limit_coin_change([1,5,10,25], 37) == 0
    assert ways_limit_coin_change([1,1,5,10,25], 37) == 1

