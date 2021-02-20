def mirror(li):
        li=sorted(li)
        return li if len(li)<2 else li+list(reversed(li))[1:]
