

def add(num1, num2):
    l1 = list(str(num1))
    l1.reverse()
    l2 = list(str(num2))
    l2.reverse()
    l = []
    if len(l1) >= len(l2):
        ran = len(l1)
    else:
        ran = len(l2)
    for i in range(ran):
        try:
            l.append(str(int(l1[i])+int(l2[i])))
        except:
            if len(l1) > len(l2):
                l.append(l1[i])
            else:
                l.append(l2[i])
    l.reverse()
    return int(''.join(l))
