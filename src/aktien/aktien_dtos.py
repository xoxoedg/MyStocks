class AktienAuswahlResponseDto:
    id: int = 0
    name: str = ""

    def serialize(self) -> dict:
        return {
            "lookup_id": self.id,
            "name": self.name,
        }


class SelectedAktie:

    def __init__(self, lookup_id, name):
        self.lookup_id = lookup_id
        self.name = name


class AuswahlBestaetigenRequestDto:

    def __init__(self, json):
        self.selected_aktien = []
        selected_aktien = json['selectedAktien']
        for aktie in selected_aktien:
            self.selected_aktien.append(SelectedAktie(aktie['lookup_id'], aktie['name']))
