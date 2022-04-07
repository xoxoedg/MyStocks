from requests_tor import RequestsTor
import requests


class RequestBuilder:

    def __init__(self):
        self.tor_request = RequestsTor()

    def get_request(self, url):
        return requests.get(url=url)

    def post_request(self, url, body):
        return requests.post(url=url, data=body)
