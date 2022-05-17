import json
import os

from src import db
from src.administration.lookup.lookup import LookUp
from src.aktien.aktie import Aktie
from src.common.decoraters.decorators import db_exception_handling

STATISTICS_PREFIX = 'statistics_'


class MockService:

    @db_exception_handling
    def get_mock_statistics_data(self, selected_aktie):
        lookup_id = selected_aktie.lookup_id
        lookup = LookUp.query.get(lookup_id)
        filename = STATISTICS_PREFIX + lookup.api_name + '.json'
        data_file_path = os.path.join(os.path.dirname(__file__), filename)

        statistics = json.load(open(data_file_path))
        aktueller_preis = statistics['price']['regularMarketPrice']['fmt']
        aktie = Aktie(lookup_id=lookup_id, aktueller_preis=aktueller_preis, aktiv=True)
        db.session.add(aktie)
        db.session.commit()
