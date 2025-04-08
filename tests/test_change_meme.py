import pytest

from test_API_meme.data_for_tests import data_for_update, data_param_change_meme


def test_change_url_of_meme(authorisation, change_meme_endpoint, create_meme_id_then_delete_it):
    meme_id = create_meme_id_then_delete_it
    data_for_update.update({'id': meme_id, 'url':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaL5H038UJ0ZktVJ4Z5jWNLuAQzjRFAjgPw&s'})
    change_meme_endpoint.change_meme(meme_id, payload=data_for_update, headers=authorisation.get_headers())
    change_meme_endpoint.check_status_code_is_200()

def test_change_text_of_meme_with_invalid_id(authorisation, non_existing_meme_id, change_meme_endpoint):
    meme_id = non_existing_meme_id
    data_for_update.update({'id': meme_id, 'text': 'new_text'})
    change_meme_endpoint.change_meme(meme_id, payload=data_for_update, headers=authorisation.get_headers())
    change_meme_endpoint.check_status_code_is_404()
    change_meme_endpoint.check_response_text_not_found()

def test_change_meme_without_auth(authorisation, create_meme_id_then_delete_it, change_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    data_for_update.update({'id': meme_id, 'text': 'new_text'})
    change_meme_endpoint.change_meme(meme_id, payload=data_for_update, headers='')
    change_meme_endpoint.check_status_code_is_401()
    change_meme_endpoint.check_response_text_unauthorized()

def test_change_meme_with_foreign_token(authorisation, create_meme_id_then_delete_it, change_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    data_for_update.update({'id': meme_id, 'text': 'new_text'})
    change_meme_endpoint.change_meme(meme_id, payload=data_for_update, headers=authorisation.get_foreign_token())
    change_meme_endpoint.check_status_code_is_401()
    change_meme_endpoint.check_response_text_unauthorized()

@pytest.mark.parametrize(('url_data', 'info_data'), data_param_change_meme)
def test_change_url_info_with_invalid_data(authorisation, create_meme_id_then_delete_it, change_meme_endpoint, url_data, info_data):
    meme_id = create_meme_id_then_delete_it
    data_for_update.update({'id': meme_id, 'info': info_data, 'url': url_data})
    change_meme_endpoint.change_meme(meme_id, payload=data_for_update, headers=authorisation.get_headers())
    change_meme_endpoint.check_status_code_is_400()