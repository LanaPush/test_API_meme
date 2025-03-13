import requests

def get_token():
    headers = {'Content-Type': 'application/json'}
    payload = {'name': 'ichbin'}
    response = requests.post(
        url='http://167.172.172.115:52355/authorize',
        headers=headers,
        json=payload
    ).json()
    return response['token']

token = get_token()

def check_token_is_alive():
    response = requests.get(url=f'http://167.172.172.115:52355/authorize/{token}')
    return response.status_code

def auth():
    if check_token_is_alive() == 200:
        return token
    else:
        return get_token()










