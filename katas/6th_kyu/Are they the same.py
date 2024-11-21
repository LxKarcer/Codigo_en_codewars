def comp(array1, array2):
    cuadrados_array1 = []
    if (not array1 and array1 != []) or (not array2 and array2 != []):
        return False
    for numero in array1:
        if numero**2 in array2:
            cuadrados_array1.append(numero**2)
        else:
            return False
    cuadrados_array1.sort()
    array2.sort()
    return cuadrados_array1 == array2