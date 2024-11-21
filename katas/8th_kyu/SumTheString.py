def sum_str(num1 , num2):
    if num1 != '' and num2 != '': 
        int_num1 = int(num1)
        int_num2 = int(num2)
        return f'{int_num1 + int_num2}'
    elif num1 == ''and num2 == '':
        return '0'
    elif num1 == '':
        return f'{int(num2)}'
    elif num2 == '':
        return f'{int(num1)}'