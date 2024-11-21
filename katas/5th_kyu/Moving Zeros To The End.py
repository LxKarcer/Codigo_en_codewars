def move_zeros(lst):
    aux_list = []
    zero_list = []
    for number in lst:
        if number == 0:
            zero_list.append(0)
        else:
            aux_list.append(number)
    return aux_list + zero_list   