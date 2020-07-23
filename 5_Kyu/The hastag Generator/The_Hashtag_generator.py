def generate_hashtag(word):
    word = word.title()
    sp = word.split()
    if len(word) == 0 or len(word) > 140:
        return False
    else:
        return '#'+''.join(sp)
