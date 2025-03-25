import requests


from test_API_meme.endpoints.endpoints import Endpoint


class CreateMeme(Endpoint):
    def __init__(self):
        self.meme_id = None

    def create_meme_post(self, headers=None, payload=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            headers=headers,
            json=payload
        )
        self.status_code = self.response.status_code
        return self.response


    def check_meme_escape_text(self, headers=None, payload=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            headers=headers,
            json=payload
        )
        assert self.text == '&lt;script&gt;alert123&lt;/script&gt'

    def create_meme_id(self, headers=None, payload=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            headers=headers,
            json=payload
        )
        self.text = self.response.json()['text']
        self.meme_id = self.response.json()['id']
        return self.meme_id