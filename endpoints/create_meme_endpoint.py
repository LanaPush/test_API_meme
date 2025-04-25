import allure
import requests

from test_API_meme.data_for_tests import main_data
from test_API_meme.endpoints.endpoints import Endpoint


class CreateMeme(Endpoint):
    def __init__(self):
        self.meme_id = None

    @allure.step('create meme post')
    def create_meme(self, headers=None, payload=None):
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

    def check_meme_text_is_the_same(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        ).json()
        assert self.response['info'] == main_data['info']
        assert self.response['url'] == main_data['url']