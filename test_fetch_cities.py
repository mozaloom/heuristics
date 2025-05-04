from fetch_cities_lat_long import main, my_cities, create_cities_dataframe
import pytest


# test the my_cities function
def test_my_cities():
    assert my_cities("New York", "Los Angeles") == [
        "New York",
        "Los Angeles",
    ]


