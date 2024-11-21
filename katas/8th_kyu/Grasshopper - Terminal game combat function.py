def combat(health, damage):
    x = health - damage
    if x >=0:
        return x
    elif x < 0:
        return 0