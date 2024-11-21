def is_valid_walk(walk):
    north_south = []
    east_west =[]
    for coord in walk:
        if coord == "n":
            north_south.append(1)
        elif coord == "s":
            north_south.append(-1)
        elif coord == "e":
            east_west.append(1)
        elif coord == "w":
            east_west.append(-1)
        else:
            return False
        
    if sum(north_south) == 0 and sum(east_west)  == 0 and len(walk) == 10:
        return True
    else:
        return False