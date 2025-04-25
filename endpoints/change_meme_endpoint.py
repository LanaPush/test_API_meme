import allure
import requests
from test_API_meme.endpoints.endpoints import Endpoint


class ChangeMeme(Endpoint):

    @allure.step('change a meme information')
    def change_meme(self, meme_id, headers, payload):
        self.response = requests.put(
            url=f'{self.url}/meme/{meme_id}',
            headers=headers,
            json=payload
        )
        return self.response

    def check_changed_url(self, meme_id, local_data_for_update, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        ).json()
        assert self.response['url'] == local_data_for_update['url']
