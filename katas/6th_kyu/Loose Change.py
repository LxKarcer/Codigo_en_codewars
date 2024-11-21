def loose_change(money):
    nickels = 5
    pennies = 1
    dimes = 10
    quarters = 25
    Q = 0
    D = 0
    N = 0
    P = 0
    lista_monedas = [quarters, dimes, nickels, pennies]

    lista_contador = [Q, D ,N, P]

    lista_nombre_monedas = ['Quarters', 'Dimes', 'Nickels', 'Pennies']

    dinero_a_restar = money
    for coin in lista_monedas:
        while dinero_a_restar >= coin:
            dinero_a_restar = dinero_a_restar - coin
            lista_contador[lista_monedas.index(coin)] = lista_contador[lista_monedas.index(coin)] + 1
        
    vueltas = dict(zip(lista_nombre_monedas, lista_contador))
    return vueltas