import requests

from test_API_meme.endpoints.endpoints import Endpoint


class ChangeMeme(Endpoint):

    def change_meme(self, meme_id, headers, payload):
        self.response = requests.put(
            url=f'{self.url}/meme/{meme_id}',
            headers=headers,
            json=payload
        )
        return self.response