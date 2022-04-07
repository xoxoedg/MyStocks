from src.common.request_builder import RequestBuilder


class QuartalszahlenRequestBuilder(RequestBuilder):

    def __init__(self, aktien_endpoint, url):
        super().__init__()
        self.base_url = "https://www.finanzen.net/termine/"
        self.aktien_endpoint = aktien_endpoint

    def build_url(self):
        return self.base_url + self.aktien_endpoint

