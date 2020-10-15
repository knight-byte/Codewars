def ordered_count(inp):
    li=[]
    for i in inp:
        count=inp.count(i)
        if count!=0:
            li.append((i,count))
            inp=inp.replace(i,'')
    return li
