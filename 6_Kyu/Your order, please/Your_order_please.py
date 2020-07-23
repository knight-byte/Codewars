def order(word):
    ch = word.split(" ")
    tmp = [0]*len(ch)
    j = 0
    for i in range(0, len(ch)):
        for j in range(1, len(ch)+1):
            if str(j) in ch[i]:
                break
        tmp[j-1] = ch[i]
    return (" ".join(tmp))
