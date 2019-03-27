import unittest
import requests


class TestBooks(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com'
        self.part_url = '/books'
        self.book_id = None

    def test_book_create(self):
        book_data = {"title": "Mu-Mu", "author": "Ivan Turgenev"}
        res = requests.post(self.base_url + self.part_url, data=book_data)
        self.assertEqual(201, res.status_code)
        body = res.json()
        self.book_id = body['id']
        book_data['id'] = self.book_id
        self.assertEqual(body, book_data)

    def tearDown(self):
        if self.book_id is not None:
            requests.delete(f'{self.base_url}{self.part_url}/{self.book_id}')
