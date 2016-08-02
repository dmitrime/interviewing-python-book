# the least amount of coins to make change
def min_coin_change(coins, amount):
    # table to remember best solutions up to amount.
    # there is already a solution for amount of zero.
    mintable = [0] + [None]*amount

    # iterate over all coins
    for coin in coins:
        # all amounts from small to large
        for cur_amount in range(1, amount+1):
            # if we can use the coin and the table already has some value at this index
            if coin <= cur_amount and \
               mintable[cur_amount-coin] is not None:
                # assign or update to the minimum number of coins
                if mintable[cur_amount] is None or \
                   mintable[cur_amount-coin] + 1 < mintable[cur_amount]:
                    mintable[cur_amount] = mintable[cur_amount-coin] + 1

    return mintable[amount]

if __name__ == '__main__':
    print min_coin_change([3], 25)
    print min_coin_change([5, 10, 25], 101)
    print min_coin_change([1], 10)
    print min_coin_change([5, 10, 25], 100)

    assert min_coin_change([1,5,10,25], 63) == 6
    assert min_coin_change([5, 10, 25], 100) == 4
    assert min_coin_change([1], 10) == 10
    assert min_coin_change([5, 10, 25], 101) == None
    assert min_coin_change([], 10) == None
    assert min_coin_change([1,2,5], 0) == 0
    assert min_coin_change([], 0) == 0
