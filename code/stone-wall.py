# http://blog.codility.com/2012/06/sigma-2012-codility-programming.html

def min_blocks(heights):
    stack = []
    blocks = 0
    for h in heights:
        while len(stack) > 0 and stack[-1] > h:
            stack.pop()
            blocks += 1

        if len(stack) == 0 or stack[-1] < h:
            stack.append(h)

    return blocks + len(stack)

if __name__ == '__main__':
        assert min_blocks([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7
        assert min_blocks([]) == 0
        assert min_blocks([1, 1, 1]) == 1
        print min_blocks([1, 9, 2])
