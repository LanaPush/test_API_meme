import requests

from test_API_meme.endpoints.get_token import auth


def test_delete_meme_post(get_meme_id):
    headers = {'Authorization': auth()}
    response = requests.delete(f'http://167.172.172.115:52355/meme/{get_meme_id}', headers=headers)
    print(response.status_code)
    assert response.status_code == 200

def test_delete_meme_deleted_id(create_delete_meme_at_sametime):
    headers = {'Authorization': auth()}
    response = requests.delete(f'http://167.172.172.115:52355/meme/{create_delete_meme_at_sametime}', headers=headers)
    assert response.status_code == 404
    assert "404 Not Found" in response.text, f"{response.text}"

def test_delete_meme_with_foreign_token(get_meme_id, foreign_token):
    headers = {'Content-Type': foreign_token}
    response = requests.delete(f'http://167.172.172.115:52355/meme/{get_meme_id}', headers=headers)
    assert response.status_code == 401
    assert "401 Unauthorized" in response.text, f"{response.text}"

def test_delete_without_auth(get_meme_id):
    response = requests.delete(f'http://167.172.172.115:52355/meme/{get_meme_id}')
    assert response.status_code == 401
    assert "401 Unauthorized" in response.text, f"{response.text}"