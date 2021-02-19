def points(dice):
    # code your solution here
    print(dice)
    dic={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
    mi=int(dice[0])
    for i in dice:
        dic[i]+=1
    if 5 in dic.values():
        return 50
    elif 4 in dic.values():
        return 40
    elif 3 in dic.values() and 2 in dic.values():
        return 30
    elif 3 not in dic.values() and 2 in dic.values():
        return 0
    
    l=[int(i) for i in dice]
    l1=l[:]
    l2=l[:]
    if dice[0]=='1':
        l1=l[1:]
        
    elif dice[4]=='1':
        l2=l[:3]
    
    if (sorted(l) == list(range(min(l), max(l)+1))) or (sorted(l1) == list(range(min(l1), max(l1)+1))) or (sorted(l2) == list(range(min(l2), max(l2)+1))):
        return 20

        
    return 0
