def positive_sum(arr):
    # Your code here
    su=0
    for i in arr:
        if i>=0:
            su+=i 
        else:
            continue
    return su
