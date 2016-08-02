def balanced(parens):
    stack = []
    for p in parens:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0

if __name__ == '__main__':
    assert balanced('(()((())()))') == True
    assert balanced('(((()())))') == True
    assert balanced('(()))') == False
    assert balanced('') == True

