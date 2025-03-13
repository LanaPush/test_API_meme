import pytest
import requests

from test_API_meme.endpoints.endpoints import Endpoint
from test_API_meme.endpoints.get_token import auth



class Authorisation(Endpoint):
    payload_auth = {'name': 'ichbin'}
    def auth(self):
        if Endpoint.check_token_is_alive == 200:
            return self.token
        else:
            return Endpoint.get_token(self.payload_auth)


@pytest.fixture
def create_meme_post_then_delete_it():
    payload = {
        'text': 'Cat meme',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white","black"], "objects": ["test", "picture"]}
}
    headers = {'Authorization': auth()}
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    meme_id = response.json()['id']
    yield meme_id
    response_delete = requests.delete(f'http://167.172.172.115:52355/meme/{meme_id}', headers=headers)
    print(response_delete.status_code)
    print(f'\nDeleting meme with id {meme_id}')


@pytest.fixture()
def create_delete_meme_at_sametime():
    payload = {
        'text': 'Cat meme',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    meme_id = response.json()['id']
    print(f'\nMeme is created with id {meme_id}')
    requests.delete(f'http://167.172.172.115:52355/meme/{meme_id}', headers=headers)
    print(f'\nDeleting meme with id {meme_id}')

@pytest.fixture()
def get_meme_id():
    payload = {
        'text': 'Cat meme',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    meme_id = response.json()['id']
    return meme_id

@pytest.fixture()
def foreign_token():
    headers = {'Content-Type': 'application/json'}
    payload = {'name': 'jack'}
    response = requests.post(
        url='http://167.172.172.115:52355/authorize',
        headers=headers,
        json=payload
    ).json()
    return response['token']