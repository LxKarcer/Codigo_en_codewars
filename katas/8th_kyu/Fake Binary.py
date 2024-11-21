def fake_bin(x):
    list_string = list(x)
    int_list = []
    bin_list = []
    for digit in list_string:
        int_list.append(int(digit))
    for number in int_list:
        if number >= 5:
            bin_list.append(1)
        elif number < 5:
            bin_list.append(0)
    return ''.join(map(str,bin_list))
            