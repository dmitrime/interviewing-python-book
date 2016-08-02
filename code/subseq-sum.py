
def subseq_sum1(ar):
    sum_max, sum_sofar = 0, 0
    for i in range(len(ar)):
        sum_sofar = max(sum_sofar + ar[i], 0)
        sum_max = max(sum_max, sum_sofar)
    return sum_max

def subseq_sum2(ar):
    sum_all, sum_max, sum_min = 0, 0, 0
    for i in range(len(ar)):
        sum_all += ar[i]
        sum_min = min(sum_min, sum_all)
        sum_max = max(sum_max, sum_all - sum_min)
    return sum_max

if __name__ == '__main__':
    assert subseq_sum1([1, 0, -2, -3, 3, 4, 5, -5, -1, 9]) == 15
    assert subseq_sum1([-1, -2, -3, 4, -5, 1, 2]) == 4
    assert subseq_sum1([]) == 0

    assert subseq_sum2([1, 0, -2, -3, 3, 4, 5, -5, -1, 9]) == 15
    assert subseq_sum2([-1, -2, -3, 4, -5, 1, 2]) == 4
    assert subseq_sum2([]) == 0
