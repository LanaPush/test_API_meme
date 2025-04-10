import allure


@allure.feature('get meme')
def test_get_all_meme(get_meme_endpoint, authorisation):
    get_meme_endpoint.get_all_meme(headers=authorisation.get_headers())
    get_meme_endpoint.check_status_code_is_200()


@allure.feature('get meme')
def test_check_fields_in_get_response(create_meme_id_then_delete_it, authorisation, get_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    get_meme_endpoint.get_fields_in_response(meme_id, headers=authorisation.get_headers())


@allure.feature('get meme')
@allure.severity('critical')
def test_get_type_of_fields_in_response(create_meme_id_then_delete_it, authorisation, get_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    get_meme_endpoint.get_type_of_fields_in_response(meme_id, headers=authorisation.get_headers())


@allure.feature('get meme')
def test_get_meme_id(create_meme_id_then_delete_it, authorisation, get_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    get_meme_endpoint.get_meme_id(meme_id, authorisation.get_headers())
    get_meme_endpoint.check_status_code_is_200()
