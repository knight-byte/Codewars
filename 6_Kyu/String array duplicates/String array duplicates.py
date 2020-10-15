from itertools import groupby

def dup(String):
    for i in range(len(String)):
        li = list(String[i])
        remove = [k for k, _ in groupby(li)]
        String[i]=''.join(remove)
    return String
