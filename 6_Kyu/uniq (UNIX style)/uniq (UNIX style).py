def uniq(seq): 
    nli=list()
    for i in range(len(seq)):
        if  i==len(seq)-1 or seq[i]!=seq[i+1]:
            nli.append(seq[i])
            
    return nli
