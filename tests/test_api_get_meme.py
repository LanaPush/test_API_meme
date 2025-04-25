import allure


@allure.feature('get meme')
def test_get_all_meme(get_meme_endpoint, authorisation):
    get_meme_endpoint.check_get_all_meme(headers=authorisation.get_headers())
    get_meme_endpoint.check_status_code_is_200()
    get_meme_endpoint.check_meme_list_not_empty(headers=authorisation.get_headers())


@allure.feature('get meme')
def test_check_fields_in_get_response(create_meme_id_then_delete_it, authorisation, get_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    get_meme_endpoint.check_fields_in_response(meme_id, headers=authorisation.get_headers())
    get_meme_endpoint.check_type_of_fields_in_response(meme_id, headers=authorisation.get_headers())
    get_meme_endpoint.check_meme_id_is_the_same(meme_id, headers=authorisation.get_headers())

@allure.feature('get meme')
def test_get_meme_id(create_meme_id_then_delete_it, authorisation, get_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    get_meme_endpoint.get_meme_id(meme_id, headers=authorisation.get_headers())
    get_meme_endpoint.check_status_code_is_200()


@allure.feature('get meme without authorisation')
def test_get_meme_id_without_authorisation(create_meme_id_then_delete_it, get_meme_endpoint):
    meme_id = create_meme_id_then_delete_it
    get_meme_endpoint.get_meme_text(meme_id, headers=None)
    get_meme_endpoint.check_status_code_is_401()
    get_meme_endpoint.check_status_code_is_401()


@allure.feature('get non existing meme_id')
def test_get_non_existing_meme(create_meme_id, delete_meme_endpoint, get_meme_endpoint, authorisation):
    meme_id = create_meme_id
    delete_meme_endpoint.delete_meme(meme_id, headers=authorisation.get_headers())
    get_meme_endpoint.get_meme_text(meme_id, headers=authorisation.get_headers())
    get_meme_endpoint.check_status_code_is_404()
    get_meme_endpoint.check_response_text_not_found()


@allure.feature('get meme_id with foreign token')
def test_get_meme_id_with_foreign_token(authorisation, get_meme_endpoint, create_meme_id_then_delete_it):
    meme_id = create_meme_id_then_delete_it
    response = get_meme_endpoint.get_meme_text(meme_id, headers=authorisation.get_foreign_token())
    get_meme_endpoint.check_status_code_is_200()
    print(response)

