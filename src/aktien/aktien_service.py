from src import db
from src.administration.lookup.lookup import LookUp
from src.aktien.aktie import Aktie
from src.aktien.aktien_dtos import AktienAuswahlResponseDto
from src.common.decoraters.decorators import db_exception_handling


class AktienService:

    @db_exception_handling
    def get_aktien_auswahl(self):
        alle_aktien_lookups = LookUp.query.all()
        result = list(map(lambda lookup: self.to_dto(lookup).serialize(), alle_aktien_lookups))
        return result

    @db_exception_handling
    def auswahl_bestaetigen(self, selected_aktien):
        sample = selected_aktien[0]
        aktie = Aktie(lookup_id=sample.lookup_id, aktueller_preis=123.21)
        db.session.add(aktie)
        db.session.commit()

    @staticmethod
    def to_dto(lookup):
        dto = AktienAuswahlResponseDto()
        dto.id = lookup.id
        dto.name = lookup.app_name
        return dto
