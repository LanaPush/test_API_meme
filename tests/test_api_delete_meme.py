import allure


@allure.feature('delete meme')
def test_delete_meme_id(delete_meme_endpoint, create_meme_id, authorisation, get_meme_endpoint):
    meme_id = create_meme_id
    delete_meme_endpoint.delete_meme(meme_id, headers=authorisation.get_headers())
    delete_meme_endpoint.check_status_code_is_200()
    response = get_meme_endpoint.get_deleted_post(meme_id, headers=authorisation.get_headers())
    print(response)


@allure.feature('delete meme')
def test_delete_meme_id_with_foreign_meme_id(delete_meme_endpoint, create_meme_id, authorisation):
    meme_id = create_meme_id
    delete_meme_endpoint.delete_meme(meme_id, headers=authorisation.get_foreign_token())
    delete_meme_endpoint.check_status_code_is_403()
    delete_meme_endpoint.check_response_text_forbidden()


@allure.feature('delete meme')
def test_delete_meme_id_without_auth(delete_meme_endpoint, create_meme_id):
    delete_meme_endpoint.delete_meme(create_meme_id, headers='')
    delete_meme_endpoint.check_status_code_is_401()
    delete_meme_endpoint.check_response_text_unauthorized()
