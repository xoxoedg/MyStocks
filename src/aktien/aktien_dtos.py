class SelectedAktie:

    def __init__(self, name):
        self.name = name


class AuswahlBestaetigenRequestDto:

    def __init__(self, json):
        self.selected_aktien = []
        selected_aktien = json['selectedAktien']
        for aktie in selected_aktien:
            self.selected_aktien.append(SelectedAktie(aktie['name']))
