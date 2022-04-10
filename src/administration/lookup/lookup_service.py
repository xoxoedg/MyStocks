from src import db
from src.administration.lookup.lookup import LookUp
from src.administration.lookup.lookup_adapter import LookupAdapter


class LookupService:


    def get_alle_aktien(self) -> list:
        alle_aktien_lookups = LookUp.query.all()
        return list(map(lambda lookup: LookupAdapter.to_dto(lookup).serialize(), alle_aktien_lookups))

    def add_aktie_lookup(self, aktien_name_app: str, aktien_name_api: str) -> None:
        aktie_eintrag = LookUp(app_name=aktien_name_app, api_name=aktien_name_api)
        db.session.add(aktie_eintrag)
        db.session.commit()
