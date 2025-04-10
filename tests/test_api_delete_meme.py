import allure


@allure.feature('delete meme')
def test_delete_meme_id(delete_meme_endpoint, create_meme_id, authorisation):
    delete_meme_endpoint.delete_meme(create_meme_id, headers=authorisation.get_headers())
    delete_meme_endpoint.check_status_code_is_200()


@allure.feature('delete meme')
def test_delete_meme_id_with_foreign_meme_id(delete_meme_endpoint, create_meme_id, authorisation):
    delete_meme_endpoint.delete_meme(create_meme_id, headers=authorisation.get_foreign_token())
    delete_meme_endpoint.check_status_code_is_401()
    delete_meme_endpoint.check_response_text_unauthorized()


@allure.feature('delete meme')
def test_delete_meme_id_without_auth(delete_meme_endpoint, create_meme_id):
    delete_meme_endpoint.delete_meme(create_meme_id, headers='')
    delete_meme_endpoint.check_status_code_is_401()
    delete_meme_endpoint.check_response_text_unauthorized()
