import random


def generatePattern(size):
    pattern = []

    for i in range(0, size):
        pattern.append(i + 1)

    for i in range(len(pattern) - 1, 0, -1):
        j = random.randint(0, i)
        pattern[i], pattern[j] = pattern[j], pattern[i]

    return pattern


pattern = generatePattern(16)
for i in pattern:
    print(i)
