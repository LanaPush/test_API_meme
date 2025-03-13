import requests

from test_API_meme.endpoints.get_token import auth


def test_get_all_meme():
    headers = {'Authorization': auth()}
    response = requests.get(
        'http://167.172.172.115:52355/meme',
        headers=headers
    )
    assert response.status_code == 200
    assert type(response.json()) == dict

def test_get_fields_in_response(create_meme_post_then_delete_it):
    headers = {'Authorization': auth()}
    response = requests.get(
        f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}',
        headers=headers
    ).json()
    assert response['url'] == 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg'
    assert response['text'] == 'Cat meme'


def test_get_type_of_fields_in_response(create_meme_post_then_delete_it):
    headers = {'Authorization': auth()}
    response = requests.get(
        f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}',
        headers=headers
    ).json()
    assert type(response['tags']) == list
    assert type(response['text']) == str
    assert type(response['info']) == dict


