import allure
import requests
from test_API_meme.endpoints.endpoints import Endpoint


class Authorisation(Endpoint):

    @allure.step('get a token for authorisation')
    def get_token(self):
        payload = {'name': 'ichbin'}
        response = requests.post(
            url=f'{self.url}/authorize',
            headers={'Content-Type': 'application/json'},
            json=payload
        ).json()
        return response['token']

    @allure.step('check the token is alive or not')
    def auth(self):
        self.token = self.get_token()
        response_token = requests.get(url=f'{self.url}/authorize/{self.token}')
        if response_token.status_code != 200:
            self.token = self.get_token()
        return self.token

    @allure.step('make authorisation')
    def get_headers(self):
        self.headers = {'Authorization': self.auth()}
        return self.headers

    @allure.step('return a token')
    def check_token(self, payload=None):
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(
            url=f'{self.url}/authorize',
            headers=headers,
            json=payload
        )
        return self.response

    @allure.step('assert the token name is the same')
    def check_token_name(self, payload=None):
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(
            url=f'{self.url}/authorize',
            headers=headers,
            json=payload
        ).json()
        assert self.response['user'] == payload['name']

    @allure.step('get another token for some tests with authorisation')
    def get_foreign_token(self):
        payload = {'name': 'foreign token'}
        self.response = requests.post(
            url=f'{self.url}/authorize',
            headers={'Content-Type': 'application/json'},
            json=payload
        ).json()
        self.token = self.response['token']
        self.headers = {'Authorisation': self.token}
        return self.headers
