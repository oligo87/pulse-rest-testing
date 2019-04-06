import pytest
import requests


@pytest.fixture(scope="function")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com"


book_list = [{"title": "Mu-Mu", "author": "Ivan Turgenev"}]


@pytest.fixture(params=book_list, ids=[str(x) for x in book_list])
def book_data(base_url, request):
    book_data = request.param
    yield book_data
    if 'id' in book_data:
        requests.delete(f"{base_url}/books/{book_data['id']}")


new_book_data_list = [{"title": "Newest Title", "author": "Newest Author"}]


@pytest.fixture(params=new_book_data_list, ids=[str(x) for x in new_book_data_list])
def new_book_data(base_url, request):
    new_book_data = request.param
    yield new_book_data
    if 'id' in new_book_data:
        requests.delete(f"{base_url}/books/{new_book_data['id']}")

