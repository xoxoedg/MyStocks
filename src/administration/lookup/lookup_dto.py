class LookupDto:

    id: int = 0
    app_name: str = ""
    api_name: str = ""

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "app_name": self.app_name,
            "api_name": self.api_name
        }