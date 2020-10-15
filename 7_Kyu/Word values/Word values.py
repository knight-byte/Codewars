def name_value(my_list):
    li=[]
    ind=0
    print(my_list)
    for word in my_list:
        word=''.join(word.split())
        lit=[ord(a)-96 for a in word]
        s=sum(lit)
        ind+=1
        li.append(s*ind)
        
    return li
