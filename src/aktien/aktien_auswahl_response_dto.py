class AktienAuswahlResponseDto:
    id: int = 0
    name: str = ""

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
        }
