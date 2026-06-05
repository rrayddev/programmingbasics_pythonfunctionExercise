def estimate_arrival(distance_km, weather_condition):
    travel_time = distance_km * 3
    if (weather_condition == "rainy"):
        travel_time += 10
    return travel_time
distance_km = 5
weather_condition = "rainy"
print(estimate_arrival(distance_km, weather_condition), "Minutes")