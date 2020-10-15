def snail(arr):
    ret = []
    rs, re, cs, ce = 0, len(arr)-1, 0, len(arr[0])-1
    print(re, ce)
    while rs <= re and cs <= ce:
        # start row
        for i in range(cs, ce+1):
            ret.append(arr[rs][i])
        rs += 1

        # last col
        for i in range(rs, re+1):
            ret.append(arr[i][ce])
        ce -= 1

        # last row
        if rs <= re:
            for i in range(ce, cs-1, -1):
                ret.append(arr[re][i])
        re -= 1
        # first col
        if cs <= ce:
            for i in range(re, rs-1, -1):
                ret.append(arr[i][cs])
        cs += 1

    return ret
