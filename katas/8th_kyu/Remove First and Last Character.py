def remove_char(s):
    l = list(s)
    l.pop(0)
    l.pop(-1)
    
    return ''.join(l)