AtoZ = [chr(x) for x in range(ord('a'), ord('z')+1)]


def possible_words(w):
    for i in range(len(w)):
        for x in AtoZ:
            nw = w[:i] + x + w[i+1:]
            if nw != w:
                yield nw


def word_ladder(initial, target, words):
    all_words = set(words + [target])
    q = [(initial, [])]
    while len(q) > 0:
        w, path = q.pop(0)
        if w == target:
            return path + [w]
        else:
            for nw in possible_words(w):
                if nw in all_words and nw not in path:
                    q.append((nw, path + [w]))
                    #all_words.remove(nw) # works with this!
    return []


def ladderLength(initial, target, words):
    all_words = set(words + [target])
    AtoZ = [chr(x) for x in range(ord('a'), ord('z')+1)]
    q = [(initial, [])]
    while len(q) > 0:
        w, path = q.pop(0)
        if w == target:
            return path + [w]
        for i in range(len(w)):
            for x in AtoZ:
                nw = w[:i] + x + w[i+1:]
                if nw in all_words:
                    q.append((nw, path + [w]))
                    all_words.remove(nw)
    return []


if __name__ == '__main__':
    #print ladderLength(initial='dark',
                       #target='fine',
                       #words=['dare', 'fare', 'fire'])
    #print ladderLength(initial='hot',
                       #target='dog',
                       #words=[])

    assert word_ladder('dark', 'fine', ['dark', 'dare', 'fare', 'fire']) == \
        ['dark', 'dare', 'fare', 'fire', 'fine']

    assert word_ladder('star', 'rats', []) == []
