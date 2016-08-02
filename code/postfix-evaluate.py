def postfix_eval(exp):
    # possible operators and their functions
    ops = {'+': lambda a,b: a+b,
           '-': lambda a,b: a-b,
           '*': lambda a,b: a*b,
           '/': lambda a,b: a/b}
    stack = []
    # split for expression on whitespace
    # and iterate over the parts
    for p in exp.split():
        if p.isdigit(): # a number
            stack.append(int(p))
        elif p in ops.keys(): # an operator
            if len(stack) < 2:
                # operator needs 2 arguments
                return None
            num2 = stack.pop()
            num1 = stack.pop()
            res = ops[p](num1, num2) 
            stack.append(res)
        else:
            # unknown operator
            return None
    # only one value should remain in the stack
    if len(stack) != 1:
        return None
    return stack.pop()

if __name__ == '__main__':
    #print postfix_eval('1 2 + 3 4 - *')

    assert postfix_eval('1') == 1
    assert postfix_eval('1 1 -') == 0
    assert postfix_eval('1 2 + 3 4 - *') == -3
    assert postfix_eval('1 2 + 3 * 6 + 2 3 + /') == 3

    assert postfix_eval('') == None
    assert postfix_eval('1 2') == None
    assert postfix_eval('1 2 x') == None
