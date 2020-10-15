from itertools import permutations as p


def permutations(str):
    print(str)
    permList = p(str)
    li = []
    for perm in list(permList):
        li.append(''.join(perm))
    l2=list(set(li))
    l2.sort()
    return l2
