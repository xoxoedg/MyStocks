import requests


class RequestBuilder:

    def get_request(self, url):
        return requests.get(url=url)

    def post_request(self, url, body):
        return requests.post(url=url, data=body)
