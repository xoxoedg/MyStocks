class LookupDto:

    app_name: str = ""
    api_name: str = ""

    def serialize(self) -> dict:
        return {
            "app_name": self.app_name,
            "api_name": self.api_name
        }