import pytest
from test_API_meme.data_for_tests import main_data
from test_API_meme.endpoints.authorisation_endpoint import Authorisation
from test_API_meme.endpoints.change_meme_endpoint import ChangeMeme
from test_API_meme.endpoints.create_meme_endpoint import CreateMeme
from test_API_meme.endpoints.delete_meme_endpoint import DeleteMeme
from test_API_meme.endpoints.get_meme_endpont import GetMeme


@pytest.fixture()
def authorisation():
    return Authorisation()


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def get_meme_endpoint():
    return GetMeme()


@pytest.fixture()
def change_meme_endpoint():
    return ChangeMeme()


@pytest.fixture()
def create_meme_id_then_delete_it(create_meme_endpoint, delete_meme_endpoint, authorisation):
    meme_id = create_meme_endpoint.create_meme_id(payload=main_data, headers=authorisation.get_headers())
    yield meme_id
    delete_meme_endpoint.delete_meme(meme_id, headers=authorisation.get_headers())


@pytest.fixture()
def create_meme_id(create_meme_endpoint, authorisation):
    meme_id = create_meme_endpoint.create_meme_id(payload=main_data, headers=authorisation.get_headers())
    return meme_id
