from src import db
from src.administration.lookup.lookup import LookUp
from src.administration.lookup.lookup_adapter import LookupAdapter


class LookupService:

    def get_alle_lookup(self):
        alle_aktien_lookups = LookUp.query.all()
        return list(map(lambda lookup: LookupAdapter.to_dto(lookup).serialize(), alle_aktien_lookups))

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