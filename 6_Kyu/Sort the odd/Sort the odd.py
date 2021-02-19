def sort_array(source_array):
    # Return a sorted array.
    x=sorted([i  for i in source_array if i%2!=0])
    for i in source_array:
        if i%2==0:
            x.insert(source_array.index(i),i)
    return x

