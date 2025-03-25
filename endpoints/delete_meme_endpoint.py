import requests
from test_API_meme.endpoints.endpoints import Endpoint


class DeleteMeme(Endpoint):

    def delete_meme(self, meme_id, headers):
        response_delete = requests.delete(url=f'{self.url}/meme/{meme_id}', headers=headers)
        return response_delete