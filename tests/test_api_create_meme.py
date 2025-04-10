import allure
import pytest
from test_API_meme.data_for_tests import  main_data, data_param_creating_meme


@allure.feature('create meme')
def test_create_meme_with_status_200(create_meme_endpoint, authorisation):
    create_meme_endpoint.create_meme_post(payload=main_data, headers=authorisation.get_headers())
    create_meme_endpoint.check_status_code_is_200()


@allure.feature('create meme')
def test_create_meme_without_required_field_info(create_meme_endpoint, authorisation):
    local_main_data = main_data.copy()
    local_main_data.pop('info')
    create_meme_endpoint.create_meme_post(payload=local_main_data, headers=authorisation.get_headers())
    create_meme_endpoint.check_status_code_is_400()
    create_meme_endpoint.check_response_text_bad_request()


@allure.feature('create meme')
def test_create_meme_without_required_field_url(create_meme_endpoint, authorisation):
    local_main_data = main_data.copy()
    local_main_data.pop('url')
    create_meme_endpoint.create_meme_post(payload=local_main_data, headers=authorisation.get_headers())
    create_meme_endpoint.check_status_code_is_400()
    create_meme_endpoint.check_response_text_bad_request()


@allure.feature('create meme')
@pytest.mark.parametrize('text_data, tags_data', data_param_creating_meme)
def test_create_meme_post_with_invalid_text_field(create_meme_endpoint, authorisation, text_data, tags_data):
    local_main_data = main_data.copy()
    local_main_data.update({'text': text_data, 'tags': tags_data})
    create_meme_endpoint.create_meme_post(payload=local_main_data, headers=authorisation.get_headers())
    create_meme_endpoint.check_status_code_is_400()
    create_meme_endpoint.check_response_text_bad_request()


@allure.feature('create meme')
@allure.severity('critical')
def test_create_meme_post_with_escape_string(create_meme_endpoint, authorisation):
    local_main_data = main_data.copy()
    local_main_data.update({'text': '<script>alert123</script>'})
    create_meme_endpoint.check_meme_escape_text(payload=local_main_data, headers=authorisation.get_headers())


@allure.feature('create meme')
@allure.severity('critical')
def test_create_meme_post_with_100000_symbols(create_meme_endpoint, authorisation):
    local_main_data = main_data.copy()
    local_main_data.update({'text': 'w' * 100000})
    create_meme_endpoint.create_meme_post(payload=local_main_data, headers=authorisation.get_headers())
    print(f'\nActual status_code is {create_meme_endpoint.status_code}')
    create_meme_endpoint.check_status_code_is_400()
