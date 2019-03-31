import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com"


book_list = [{"title": "Mu-Mu", "author": "Ivan Turgenev"},
             {"title": "Mu-Mu 2", "author": "Ivan Turgenev"},
             {"title": "Mu-Mu 3", "author": "Ivan Turgenev"}]


@pytest.fixture(params=book_list, ids=[str(x) for x in book_list])
def book_data(base_url, request):
    book_data = request.param
    yield book_data
    if 'id' in book_data:
        requests.delete(f"{base_url}/books/{book_data['id']}")


# @pytest.fixture
# def wrong_book_data():
#     book_data = {"title": "Mu-Mu",
#                  "author": ""}
#     return book_data
