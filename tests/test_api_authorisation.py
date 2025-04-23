import allure
import pytest
from test_API_meme.data_for_tests import auth_data, auth_invalid_data


@allure.feature('authorisation')
@pytest.mark.parametrize('invalid_data', auth_invalid_data)
def test_authorisation_with_invalid_name(invalid_data, authorisation):
    authorisation.check_token(invalid_data)
    authorisation.check_status_code_is_400()


@allure.feature('authorisation')
@allure.severity('critical')
def test_authorisation_status_code_200(authorisation):
    authorisation.check_token(auth_data)
    token = authorisation.get_token()
    authorisation.check_token_is_alive_or_not(token)
    authorisation.check_status_code_is_200()


@allure.feature('authorisation')
def test_authorisation_with_two_names_in_one_request(authorisation):
    local_auth_data = auth_data.copy()
    local_auth_data.update({'name': 'Jack', 'Surname': 'Jack'})
    authorisation.check_token_name(local_auth_data)
