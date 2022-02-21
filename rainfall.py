def get_rainfall():
    rainfall = {}
    while True:
        city = input("Enter the name of the city here: ")
        if not city:
            break

        amount_of_rain = input("Enter the amount of rainfall (in mm) here: ")
    rainfall[city] = rainfall.get(city, 0) + int(amount_of_rain)

    for city, rain in rainfall.items():
        print(f"{city}: {rain}")
    
get_rainfall()