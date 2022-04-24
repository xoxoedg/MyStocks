from src.administration.lookup.lookup import LookUp


def test_new_lookup():
    lookup = LookUp()
    lookup.api_name = "Adidas"
    lookup.app_name = "ADL S"
    assert lookup.api_name == "Adidas"
    assert lookup.app_name == "ADL S"
