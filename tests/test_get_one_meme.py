import pytest
import requests

from test_API_meme.endpoints.get_token import auth


def test_get_one_meme(create_meme_post_then_delete_it):
    headers = {'Authorization': auth()}
    response = requests.get(
        f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}',
        headers=headers
    )
    assert response.status_code == 200
    assert type(response.json()) == dict

def test_get_404_if_meme_not_found(create_delete_meme_at_sametime):
    headers = {'Authorization': auth()}
    response = requests.get(
        f'http://167.172.172.115:52355/meme/{create_delete_meme_at_sametime}',
        headers=headers
    )
    assert response.status_code == 404
    assert "404 Not Found" in response.text, f"{response.text}"

def test_get_404_without_authorisation(create_meme_post_then_delete_it):
    response = requests.get(f'http://167.172.172.115:52355/meme/{create_meme_post_then_delete_it}')
    assert response.status_code == 401
    assert "401 Unauthorized" in response.text, f'{response.text}'

#failed
def test_get_meme_with_invalid_id(create_meme_post_then_delete_it):
    headers = {'Authorization': auth()}
    response = requests.get(
        f'http://167.172.172.115:52355/meme/ichbin',
        headers=headers
    )
    assert response.status_code == 404
    assert "404 Invalid ID" in response.text, f"{response.text}"


