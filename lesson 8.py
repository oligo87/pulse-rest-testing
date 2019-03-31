import requests
import pytest


def test_book_create(base_url, book_data):
    response = requests.post(f"{base_url}/books", data=book_data)
    assert 201 == response.status_code
    body = response.json()
    book_data["id"] = body["id"]
    assert book_data == body


wrong_books_list = [({"title": "Mu-Mu", "author": ""}, {'author': ['This field may not be blank.']}),
               ({"title": "", "author": "Ivan Turgenev"}, {'title': ['This field may not be blank.']})]


# @pytest.mark.xfail(raises=ValueError, strict=True)
@pytest.mark.parametrize('wrong_book_data, expected_body', wrong_books_list, ids=[str(x[0]) for x in wrong_books_list])
def test_neg_book_create(base_url, wrong_book_data, expected_body):
    response = requests.post(f"{base_url}/books", data=wrong_book_data)
    # raise ValueError('not correct')
    assert 400 == response.status_code
    body = response.json()
    assert body == expected_body
    # assert ['This field may not be blank.'] in body.values()

    # if body.get('id'):
    #     wrong_book_data['id'] = body['id']
