
# https://en.wikipedia.org/wiki/Fizz_buzz
def fizzbuzz(n):
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('Fizz Buzz')
        elif i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res

if __name__ == '__main__':
    #print fizzbuzz(3)
    assert fizzbuzz(0) == []
    assert fizzbuzz(3) == ['1', '2', 'Fizz']
    assert fizzbuzz(15) == \
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']
