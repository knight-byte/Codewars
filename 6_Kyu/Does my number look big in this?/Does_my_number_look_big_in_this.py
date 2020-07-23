def narcissistic(value):
    l = len(str(value))
    cal = (int(x)**l for x in str(value))
    if sum(cal) == value:
        return True
    return False
