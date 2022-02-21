RATES = {'Chico': 0.5, 'Groucho': 0.7, 'Harpo': 0.5, 'Zeppo': 0.4}

def time_percentage(hour):
    return hour/24


def calculate_tax(cost, province, hour):
    return cost + (cost * RATES[province] * time_percentage(hour))



