from src import db
from src.administration.lookup.lookup import LookUp


class LookupService:


    def get_alle_aktien(self):
        return LookUp.query.all()

    def add_aktie_lookup(self, aktien_name_app, aktien_name_api):
        aktie_eintrag = LookUp(app_name=aktien_name_app, api_name=aktien_name_api)
        db.session.add(aktie_eintrag)
        db.session.commit()
