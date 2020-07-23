def solve(arr):
    arr.reverse()
    re = []
    for i in arr:
        if i not in re:
            re.append(i)

    re.reverse()
    return re
