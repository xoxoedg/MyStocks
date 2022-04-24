from common.decoraters.decorators import db_exception_handling
from common.dtos.success_dto import SuccessDto
from src import db
from src.administration.lookup.lookup import LookUp
from src.administration.lookup.lookup_adapter import LookupAdapter
from src.common.exception_handling import StocksValueException, StocksNotFoundError


class LookupService:

    @db_exception_handling
    def get_alle_lookup(self):
        alle_aktien_lookups = LookUp.query.all()
        result = list(map(lambda lookup: LookupAdapter.to_dto(lookup).serialize(), alle_aktien_lookups))
        return result

    @db_exception_handling
    def add_aktie_lookup(self, data):
        aktie_eintrag = LookUp(app_name=data["app_name"], api_name=data["api_name"])
        db.session.add(aktie_eintrag)
        db.session.commit()
        return SuccessDto("Eintrag wurde erfolgreich angelegt")

    @db_exception_handling
    def bearbeite_lookup(self, data):
        if data["id"] is not None:
            lookup_eintrag = LookUp.query.get(data["id"])
            lookup_eintrag.app_name = data["app_name"]
            lookup_eintrag.api_name = data["api_name"]
            db.session.add(lookup_eintrag)
            db.session.commit()
            return SuccessDto("Eintrag wurde erfolgreich geupdated")
        else:
            raise StocksNotFoundError("Sorry diese Aktie steht nicht zur Verfügung")

    @db_exception_handling
    def loesche_lookup(self, aktie):
        if aktie.strip() is not None:
            lookup_eintrag = LookUp.query.get(aktie)
            db.session.delete(lookup_eintrag)
            db.session.commit()
            return SuccessDto("Eintrag wurde erfolgreich gelöscht")
        else:
            raise StocksNotFoundError("Sorry diese Aktie steht nicht zur Verfügung")


    @db_exception_handling
    def get_specific_lookup(self, name):
        specific_aktie = LookUp.query.filter_by(app_name=name).first()
        if specific_aktie is not None:
           return LookupAdapter.to_dto(specific_aktie).serialize()
        else:
            raise StocksNotFoundError("Sorry diese Aktie steht nicht zur Verfügung")

