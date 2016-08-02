def atoz():
    return [chr(c) for c in range(ord('a'), ord('z')+1)]

if __name__ == '__main__':
    #print atoz()
    assert atoz() == \
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
