def decode(w):
    li = []
    key = [i for i in "abdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqH"]
    for i in range(len(w)):
        c = w[i]
        if c in key:
            li.append(key[(key.index(c) + 65 - i) % 66])
        else:
            li.append(c)
    return "".join(li)
