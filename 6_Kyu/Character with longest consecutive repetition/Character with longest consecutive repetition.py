def longest_repetition(chars):
    n = len(chars) 
    count = 0
    res = '' 
    cur_count = 1

    for i in range(n): 
        if (i < n - 1 and 
            chars[i] == chars[i + 1]): 
            cur_count += 1

        else: 
            if cur_count > count: 
                count = cur_count 
                res = chars[i] 
            cur_count = 1
    return (res,count) 
