import random

def randomize(values):
    for i in reversed(range(1, len(values))):
        r = random.randint(0, i) #!! [0, i]
        values[r], values[i] = values[i], values[r]
    return values

def randomize_py(values):
    random.shuffle(values)
    return values

if __name__ == '__main__':
    print(randomize([1, 2, 3, 4 ,5]))
    print randomize_py([1, 2, 3, 4 ,5])


