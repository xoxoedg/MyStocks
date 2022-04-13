from src import db, testing
from src.administration.lookup.lookup import LookUp
from src.administration.lookup.lookup_adapter import LookupAdapter
from src.common.exception_handling import StocksValueException


class LookupService:

    def get_alle_lookup(self):
        alle_aktien_lookups = LookUp.query.all()
        if testing:
            raise StocksValueException("This is an invalid value!")
        result = list(map(lambda lookup: LookupAdapter.to_dto(lookup).serialize(), alle_aktien_lookups))
        return result

    def add_aktie_lookup(self, data):
        aktie_eintrag = LookUp(app_name=data["app_name"], api_name=data["api_name"])
        db.session.add(aktie_eintrag)
        db.session.commit()

    def bearbeite_lookup(self, data):
        lookup_eintrag = LookUp.query.get(data["app_name"])
        lookup_eintrag.app_name = data["app_name"]
        lookup_eintrag.api_name = data["api_name"]
        db.session.add(lookup_eintrag)
        db.session.commit()

    def loesche_lookup(self, aktie):
        lookup_eintrag = LookUp.query.get(aktie)
        print(lookup_eintrag)
        db.session.delete(lookup_eintrag)
        db.session.commit()
