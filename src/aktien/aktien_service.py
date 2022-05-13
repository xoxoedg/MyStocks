from src.administration.lookup.lookup import LookUp
from src.aktien.aktien_auswahl_response_dto import AktienAuswahlResponseDto
from src.common.decoraters.decorators import db_exception_handling


class AktienService:

    @db_exception_handling
    def get_aktien_auswahl(self):
        alle_aktien_lookups = LookUp.query.all()
        result = list(map(lambda lookup: self.to_dto(lookup).serialize(), alle_aktien_lookups))
        return result

    @db_exception_handling
    def auswahl_bestaetigen(self, data):
        pass

    @staticmethod
    def to_dto(lookup):
        dto = AktienAuswahlResponseDto()
        dto.id = lookup.id
        dto.name = lookup.app_name
        return dto
