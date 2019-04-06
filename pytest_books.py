import requests
import pytest


def test_book_create(base_url, book_data):
    post_response = requests.post(f"{base_url}/books", data=book_data)
    assert 201 == post_response.status_code
    post_body = post_response.json()
    book_data["id"] = post_body["id"]
    assert book_data == post_body
    get_response = requests.get(f"{base_url}/books/{post_body['id']}")
    get_body = get_response.json()
    assert book_data == get_body
    get_list_response = requests.get(f"{base_url}/books")
    books_list = get_list_response.json()
    for book in books_list:
        if book['id'] == post_body['id']:
            book_from_list = book
    assert book_data == book_from_list


wrong_books_list = [({"title": "Mu-Mu", "author": ""}, {'author': ['This field may not be blank.']}),
                    ({"title": "", "author": "Ivan Turgenev"}, {'title': ['This field may not be blank.']}),
                    ({"field_name": "Mu-Mu", "author": "Ivan Turgenev"}, {'title': ['This field is required.']}),
                    ({"title": "Mu-Mu", "field_name": "Ivan Turgenev"}, {'author': ['This field is required.']})]


@pytest.mark.parametrize('wrong_book_data, expected_body', wrong_books_list, ids=[str(x[0]) for x in wrong_books_list])
def test_neg_book_create(base_url, wrong_book_data, expected_body):
    response = requests.post(f"{base_url}/books", data=wrong_book_data)
    assert 400 == response.status_code
    body = response.json()
    assert expected_body == body


def test_update_book(base_url, book_data, new_book_data):
    response = requests.post(f"{base_url}/books", data=book_data)
    body = response.json()
    put_response = requests.put(f"{base_url}/books/{body['id']}", data=new_book_data)
    assert 201 == response.status_code
    put_body = put_response.json()
    new_book_data["id"] = put_body["id"]
    assert new_book_data == put_body
    get_response = requests.get(f"{base_url}/books/{body['id']}")
    get_body = get_response.json()
    assert new_book_data == get_body
    get_list_response = requests.get(f"{base_url}/books")
    books_list = get_list_response.json()
    for book in books_list:
        if book['id'] == body['id']:
            book_from_list = book
    assert new_book_data == book_from_list


def test_delete_book(base_url, book_data):
    response = requests.post(f"{base_url}/books", data=book_data)
    body = response.json()
    del_response = requests.delete(f"{base_url}/books/{body['id']}")
    assert 204 == del_response.status_code
    get_response = requests.get(f"{base_url}/books/{body['id']}")
    assert 404 == get_response.status_code
    get_list_response = requests.get(f"{base_url}/books")
    books_list = get_list_response.json()
    for book in books_list:
        assert body['id'] != book['id']
