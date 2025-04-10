import allure
import requests
from test_API_meme.endpoints.endpoints import Endpoint


class CreateMeme(Endpoint):
    def __init__(self):
        self.meme_id = None

    @allure.step('create meme post')
    def create_meme_post(self, headers=None, payload=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            headers=headers,
            json=payload
        )
        self.status_code = self.response.status_code
        return self.response

    @allure.step('create meme with escape text.')
    def check_meme_escape_text(self, headers=None, payload=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            headers=headers,
            json=payload
        )
        response_status_code = self.response.status_code
        print(f'\nActual status_code is{response_status_code}')
        assert response_status_code == 400
        assert self.text == '&lt;script&gt;alert123&lt;/script&gt'


    @allure.step('create meme id')
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
