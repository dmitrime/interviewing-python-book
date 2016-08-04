def search(nums, key):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = lo + (hi - lo) / 2
        #print "lo={}, mid={}, hi={}".format(lo, mid, hi)
        if nums[mid] == key:
            return True
        elif nums[mid] < key:
            lo = mid+1
        else:
            hi = mid-1
    return False


if __name__ == '__main__':
    #assert search([], 1) == False
    assert search([0], 1) == False
    assert search(range(100), 1) == True
    assert search(range(10, 100), 1) == False
    assert search(xrange(1000000000), 987654321) == True
    assert search(xrange(1000000000), 999999999) == True
    assert search(xrange(1000000000), 0) == True
