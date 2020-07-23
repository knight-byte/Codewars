def solve(arr):
    sar = [z for z in arr]
    sar.sort()
    sar.reverse()
    print(sar)
    print(arr)
    if arr == sorted(sar):
        return 'A'
    elif arr == sar:
        return 'D'
    else:
        i = 0
        while len(arr) != 0:
            l = len(arr)
            arr.pop(i)
            sar.pop(l-1)
            if arr == sorted(sar):
                return 'RA'
            elif arr == sar:
                return 'RD'
