import requests
import pytest

from test_API_meme.endpoints.get_token import auth


#failed last name_data
@pytest.mark.parametrize('name_data', [{'name': 123}, {'name': True}, { }, {'name': 'Jack', 'surname': 'Jackson'}])
def test_authorisation_with_invalid_name(name_data):
    headers = {'Content-Type': 'application/json'}
    payload = name_data
    response = requests.post(
        url='http://167.172.172.115:52355/authorize',
        headers=headers,
        json=payload
    )
    assert response.status_code == 400
    assert "400 Bad Request" in response.text, f'{response.text}'

def test_authorization_status_code_200():
    headers = {'Content-Type': 'application/json'}
    payload = {'name': 'Jack'}
    response = requests.post(
        url='http://167.172.172.115:52355/authorize',
        headers=headers,
        json=payload
    )
    assert response.status_code == 200

