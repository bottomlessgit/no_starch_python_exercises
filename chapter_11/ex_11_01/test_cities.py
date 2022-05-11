import unittest

from city_function import get_formatted_location

class LocationTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""

    def test_city_country(self):
        """Do locations like 'Santiago, Chile' work?"""
        formatted_location = get_formatted_location("santiago", "chile")
        self.assertEquals(formatted_location, "Santiago, Chile")

unittest.main()
