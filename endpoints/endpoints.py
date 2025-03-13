import requests


class Endpoint:
    url = 'http://167.172.172.115:52355'
    json = None
    headers = None
    token = None
    payload = None


    def get_token(self, payload):
        response = requests.post(
            url='http://167.172.172.115:52355/authorize',
            headers={'Content-Type': 'application/json'},
            json=payload
        ).json()
        self.token = response['token']
        return self.token

    def check_token_is_alive(self):
        response = requests.get(url=f'http://167.172.172.115:52355/authorize/{self.token}')
        return response.status_code

