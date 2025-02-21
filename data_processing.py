def spot_labeling(spot):
    """Labels the parking size"""
    if spot is not None :
            return "Big" if spot >=200 and spot is not None else "Small"      
    return "N/A"

def none_value_labeling(value):
      """Test and look if the value is none to return N/A in the positive case"""
      return value if value is not None else "N/A"