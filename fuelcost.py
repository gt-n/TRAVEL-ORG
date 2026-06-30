def fuel_cost(total_km, mileage, fuel_rate):
    fuel_needed = total_km / mileage
    cost = fuel_needed * fuel_rate
    return cost
