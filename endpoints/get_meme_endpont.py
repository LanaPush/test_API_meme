import allure
import requests
from test_API_meme.endpoints.endpoints import Endpoint


class GetMeme(Endpoint):

    @allure.step('get list with all meme and check the type of objects')
    def get_all_meme(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/meme',
            headers=headers
        )
        assert type(self.response.json()) == dict

    @allure.step('check the attributes content of properties in object')
    def get_fields_in_response(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        assert self.response.json()['url'] == 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg'
        assert self.response.json()['text'] == 'Cat meme'

    @allure.step('check the attributes type of properties in object')
    def get_type_of_fields_in_response(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        response = requests.get(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            headers=headers
        ).json()
        assert type(response['tags']) == list
        assert type(response['text']) == str
        assert type(response['info']) == dict

    @allure.step('get meme id')
    def get_meme_id(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        return self.response.json()['id']
