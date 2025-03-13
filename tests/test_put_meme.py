import pytest
import requests

from test_API_meme.endpoints.get_token import auth


def test_change_url_of_meme(create_meme_post_then_delete_it):
    payload = {
        'id': create_meme_post_then_delete_it,
        'text': 'Cat meme',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaL5H038UJ0ZktVJ4Z5jWNLuAQzjRFAjgPw&s',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.put(
        url=f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}',
        headers=headers,
        json=payload
    )
    assert response.status_code == 200


def test_change_text_of_meme_with_not_existing_id(create_delete_meme_at_sametime):
    payload = {
        'id': create_delete_meme_at_sametime,
        'text': 'Cat meme',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaL5H038UJ0ZktVJ4Z5jWNLuAQzjRFAjgPw&s',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.put(
        url=f'http://167.172.172.115:52355/meme/{create_delete_meme_at_sametime}',
        headers=headers,
        json=payload
    )
    assert response.status_code == 404
    assert '404 Not Found' in response.text, f'{response.text}'


def test_change_text_of_meme_with_invalid_id():
    payload = {
        'id': 'Jack',
        'text': 'Cat meme',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaL5H038UJ0ZktVJ4Z5jWNLuAQzjRFAjgPw&s',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    headers = {'Authorization': auth()}
    response = requests.put(
        url='http://167.172.172.115:52355/meme/Jack',
        headers=headers,
        json=payload
    )
    assert response.status_code == 404
    assert '404 Not Found' in response.text, f'{response.text}'

#failed
parameters = {
    'url_data': [{'url': 123}, {'url': ' '}, {'url': True}, {'url': { }}],
    'info_data': [{'info': 123}, {'info': ''}, {'info': True}, {'info': []}, {'info': 'Jack'}]
              }
data_param = [(key, el) for key, nums in parameters.items() for el in nums]
@pytest.mark.parametrize('url_data, info_data', data_param)
def test_change_url_info_with_invalid_data(create_meme_post_then_delete_it, url_data, info_data):
    payload = {
        'id': create_meme_post_then_delete_it,
        'text': 'Cat meme',
        'url': url_data,
        'tags': ["funny", "cats", "work"],
        'info': info_data
    }
    headers = {'Authorization': auth()}
    response = requests.put(
        url=f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}',
        headers=headers,
        json=payload
    )
    print(response.status_code)
    assert response.status_code == 400
    assert '400 Bad Request' in response.text, f'{response.text}'

def test_change_meme_with_foreign_token(create_meme_post_then_delete_it, foreign_token):
    headers = {'Content-Type': foreign_token}
    payload = {
        'id': create_meme_post_then_delete_it,
        'text': 'Cat meme',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaL5H038UJ0ZktVJ4Z5jWNLuAQzjRFAjgPw&s',
        'tags': ["funny", "cats", "hobby"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    response = requests.put(
        url=f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}',
        headers=headers,
        json=payload
    )
    assert response.status_code == 401
    assert "401 Unauthorized" in response.text, f"{response.text}"

def test_change_meme_without_auth(create_meme_post_then_delete_it):
    payload = {
        'id': create_meme_post_then_delete_it,
        'text': 'Cat meme',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaL5H038UJ0ZktVJ4Z5jWNLuAQzjRFAjgPw&s',
        'tags': ["funny", "cats", "hobby"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }
    response = requests.put(
        url=f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}',
        json=payload
    )
    assert response.status_code == 401
    assert "401 Unauthorized" in response.text, f"{response.text}"