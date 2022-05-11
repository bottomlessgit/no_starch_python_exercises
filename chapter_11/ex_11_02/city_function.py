def get_formatted_location(city, country, population = ""):
    """Generate neatly formatted location string"""
    if population:
        location = (city.title() + ", " + country.title() + 
                    " - population " + str(population))
    else:
        location = (city.title() + ", " + country.title())
    return location
