import pytest
import requests

from test_API_meme.endpoints.get_token import auth


def test_create_meme_post_status_code_200():
    payload = {
        'text': 'Cat meme',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        url='http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    assert response.status_code == 200

def test_create_post_without_required_field_info():
    payload = {
        'text': 'Cat meme',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"]
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        url='http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    assert response.status_code == 400
    assert '400 Bad Request' in response.text, f'{response.text}'

def test_create_post_without_required_field_url():
    payload = {
        'text': 'Cat meme',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        url='http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    assert response.status_code == 400
    assert '400 Bad Request' in response.text, f'{response.text}'


parameters = {
    'text_data': [{'text': 123}, {'text': ' '}, {'text': True}, {'text': { }}],
    'tags_data': [{'tags': 123}, {'tags': ''}, {'tags': True}, {'tags': { }}, {'tags': 'Jack'}],
              }
data_param = [(key, el) for key, nums in parameters.items() for el in nums]
@pytest.mark.parametrize('text_data, tags_data', data_param)
def test_create_meme_post_with_invalid_text_field(text_data, tags_data):
    payload = {
        'text': text_data,
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': tags_data,
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        url='http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    assert response.status_code == 400
    assert '400 Bad Request' in response.text, f'{response.text}'

#failed
def test_create_post_with_shield_string():
    payload = {
        'text': '<script>alert123</script>',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        url='http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    print(response.status_code)
    print(response.json()['text'])
    assert response.json()['text'] == '&lt;script&gt;alert123&lt;/script&gt'

#failed
def test_create_post_with_100000_symbols_in_text():
    payload = {
        'text': 'W' * 100000,
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.post(
        url='http://167.172.172.115:52355/meme',
        headers=headers,
        json=payload
    )
    meme_id = response.json()['id']
    print(response.status_code)
    try:
        assert response.status_code == 400
    finally:
        requests.delete(f'http://167.172.172.115:52355/meme/{meme_id}', headers=headers)
