import unittest

from city_function import get_formatted_location

class LocationTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""

    def test_city_country(self):
        """Do locations like 'Santiago, Chile' work?"""
        formatted_location = get_formatted_location(
            "santiago",
            "chile"
        )
        self.assertEqual(
            formatted_location,
             "Santiago, Chile"
        )

    def test_city_country_population(self):
        """Do locations like 'Santiago, Chile - population 5000000' work?"""
        formatted_location = get_formatted_location(
            "santiago", 
            "chile", 
            5000000,
        )
        self.assertEqual(
            formatted_location, 
            "Santiago, Chile - population 5000000"
        )

unittest.main()
