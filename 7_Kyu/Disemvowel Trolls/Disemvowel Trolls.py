def disemvowel(string):
    return "".join([i for i in string if i.lower() not in 'aeiou'])
