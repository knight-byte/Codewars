def find_ways(m, n):
    if n == 0:
        return (0)
    else:
        m = m+n-1
        n = n-1
        c = 1
        b = 1
        for i in range(0, n):
            c = c*(m-i)
            b = b*(i+1)

        return(int(c/b))
