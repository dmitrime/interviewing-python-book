import random

def mergesort(numbers):
    N = len(numbers)
    aux = [0]*N
    # Use the auxillary list to merge
    # two sublists (lo..mid and mid+1..hi)
    # in correct order.
    def _merge(lo, mid, hi):
        # first copy the range to aux
        for k in xrange(lo, hi+1):
            aux[k] = numbers[k]
        # merge the two sublists into numbers[lo..hi]
        i, j = lo, mid+1
        for k in xrange(lo, hi+1):
            if i > mid:
                numbers[k] = aux[j]
                j += 1
            elif j > hi:
                numbers[k] = aux[i]
                i += 1
            elif aux[i] <= aux[j]:
                numbers[k] = aux[i]
                i+= 1
            else:
                numbers[k] = aux[j]
                j += 1
    # recursively partition the list
    def _recursive_sort(lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi-lo) / 2
        # sort the left half
        _recursive_sort(lo, mid)
        # sort the right half
        _recursive_sort(mid+1, hi)
        # merge left and right together
        _merge(lo, mid, hi)

    _recursive_sort(0, N-1)
    return numbers

if __name__ == '__main__':
    nums = list(reversed(range(100)))
    assert mergesort(nums) == range(100)

    nums = range(100)
    random.shuffle(nums)
    assert mergesort(nums) == range(100)

