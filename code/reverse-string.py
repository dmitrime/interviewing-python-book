def reverse(s):
    return s[::-1]

def reverse_listcomp(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

if __name__ == '__main__':
    #print reverse('reverse me')
    #print reverse_listcomp('reverse me')

    assert reverse('reverse me') == 'em esrever'
    assert reverse('X') == 'X'
    assert reverse('_.-^-._') == '_.-^-._'
