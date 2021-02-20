def is_in_middle(seq):
    # your code goes below
#     print(seq)
    seq=seq.replace('abc','X')
    if seq.count('X')==4:
        return False
    li=seq.split('X') 
    print(li)
    if len(li)<2:
        return False
    return True if len(li[0])==len(li[1]) or abs(len(li[0])-len(li[1]))==1   else False
