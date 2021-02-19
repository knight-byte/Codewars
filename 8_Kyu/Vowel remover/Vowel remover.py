def shortcut( s ):
    return "".join([i if i not in "aeiou" else "" for i in s ])
