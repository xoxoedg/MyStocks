from src import testing
from src.administration.lookup.lookup import LookUp
from src.aktien.aktie import Aktie
from src.aktien.aktien_dtos import AktienAuswahlResponseDto, AktienResponseDto
from src.aktien.mocks.mock_service import MockService
from src.common.decoraters.decorators import db_exception_handling


class AktienService:

    @db_exception_handling
    def get_aktive_aktien(self):
        aktien = Aktie.query.all()
        aktive_aktien = list(filter(lambda aktie: aktie.aktiv, aktien))
        result = list(map(lambda aktie: self.to_dto(aktie).serialize(), aktive_aktien))
        return result

    @db_exception_handling
    def get_aktien_auswahl(self):
        alle_aktien_lookups = LookUp.query.all()
        result = list(map(lambda lookup: self.to_auswahl_dto(lookup).serialize(), alle_aktien_lookups))
        return result

    @db_exception_handling
    def auswahl_bestaetigen(self, selected_aktien):
        if testing:
            mock_service = MockService()
            for selected_aktie in selected_aktien:
                mock_service.get_mock_statistics_data(selected_aktie)
        else:
            print("TODO")

    @staticmethod
    def to_dto(aktie):
        lookup = LookUp.query.get(aktie.lookup_id)
        dto = AktienResponseDto()
        dto.id = aktie.id
        dto.name = lookup.app_name
        dto.aktueller_preis = aktie.aktueller_preis
        dto.naechster_quarterly = aktie.datum_naechster_quarterly_report if aktie.datum_naechster_quarterly_report is not None else "Nicht bekannt"
        return dto

    @staticmethod
    def to_auswahl_dto(lookup):
        dto = AktienAuswahlResponseDto()
        dto.id = lookup.id
        dto.name = lookup.app_name
        return dto
