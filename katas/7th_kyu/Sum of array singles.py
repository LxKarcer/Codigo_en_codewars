def repeats(array):
    num_solitarios = []
    for number in array:
        if array.count(number) == 1:
            num_solitarios.append(number)
        else:
            continue
    return sum(num_solitarios)