def solve(s):
    up, low, num, sp = 0, 0, 0, 0
    word = list(s)
    for i in word:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        elif i.isnumeric():
            num += 1
        else:
            sp += 1
        li = [up, low, num, sp]
    return li
