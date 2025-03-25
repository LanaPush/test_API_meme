import requests

from test_API_meme.endpoints.endpoints import Endpoint


class Authorisation(Endpoint):

    def get_token(self):
        payload = {'name': 'ichbin'}
        response = requests.post(
            url=f'{self.url}/authorize',
            headers={'Content-Type': 'application/json'},
            json=payload
        ).json()
        return response['token']

    def auth(self):
        self.token = self.get_token()
        response_token = requests.get(url=f'{self.url}/authorize/{self.token}')
        if response_token.status_code != 200:
            self.token = self.get_token()
        return self.token

    def get_headers(self):
        self.headers = {'Authorization': self.auth()}
        return self.headers

    def check_token(self, payload=None):
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(
            url=f'{self.url}/authorize',
            headers=headers,
            json=payload
        )
        return self.response

    def check_token_name(self, payload=None):
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(
            url=f'{self.url}/authorize',
            headers=headers,
            json=payload
        ).json()
        assert self.response['user'] == payload['name']