from src import db
from src.administration.lookup.lookup import LookUp
from src.administration.lookup.lookup_service import LookupService


def test_get_alle_lookups(db_client):

    lookup = LookUp()
    lookup.id = 1
    lookup.api_name = "H"
    lookup.app_name = "Hello"

    db.session.add(lookup)
    db.session.commit()

    result = LookupService().get_alle_lookup()
    assert len(result) == 1
