def zero_fuel(distance_to_pump, miles_pg, fuel_left):
    if distance_to_pump <= miles_pg * fuel_left:
        return True
    else:
        return False