def get_formatted_location(city, country):
    """Generate neatly formatted location string"""
    location = city.title() + ", " + country.title()
    return location
