def invert(lst):
    new_lst = []
    for number in lst:
            new_lst.append(number - 2*number)
    return new_lst