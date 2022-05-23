class AktienAuswahlResponseDto:
    id: int = 0
    name: str = ""

    def serialize(self) -> dict:
        return {
            "lookup_id": self.id,
            "name": self.name,
        }


class SelectedAktieDto:

    def __init__(self, lookup_id, name):
        self.lookup_id = lookup_id
        self.name = name


class AuswahlBestaetigenRequestDto:

    def __init__(self, json):
        self.selected_aktien = []
        selected_aktien = json['selectedAktien']
        for aktie in selected_aktien:
            self.selected_aktien.append(SelectedAktieDto(aktie['lookup_id'], aktie['name']))


class AktienResponseDto:

    id: int = 0
    name: str = ""
    aktueller_preis: float = 0.0
    naechster_quarterly: str = ""

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "aktueller_preis": self.aktueller_preis,
            "naechster_quarterly": self.naechster_quarterly,
        }