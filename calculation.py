def ratio(int1, int2):
    """Calculation of the ratio between two values"""
    return round((int1 / int2 * 100),2)

def space_taken(spot, free_spaces):
    """Calculation of the space already occupied and the percentage of it"""
    if spot is not None and free_spaces is not None:
            taken = spot - free_spaces 
            percent = ratio(taken, spot) if spot > 0 else "N/A"
            return spot - free_spaces , percent
    return "N/A", "N/A"