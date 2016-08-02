def reverse(s):
    return s[::-1]

def reverse_sentence(sen):
    return ' '.join([reverse(s) for s in sen.split(' ')])

if __name__ == '__main__':
    print reverse_sentence('If you reverse me I will reverse you!')
    assert reverse_sentence('If you reverse me I will reverse you!') == \
        'fI uoy esrever em I lliw esrever !uoy'
