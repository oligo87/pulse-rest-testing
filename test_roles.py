import unittest
import requests


class TestRoles(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com'
        self.book_id = None
        self.book_data = {"title": "Mu-Mu", "author": "Ivan Turgenev"}
        res = requests.post(self.base_url + '/books', data=self.book_data)
        body = res.json()
        self.book_id = body['id']

    def test1_post(self):
        self.role_data = {'name': 'Hero 1', 'type': 'Supernatural', 'level': 5, 'book': self.book_id}

        r_post = requests.post(self.base_url + '/roles', data=self.role_data)
        self.role_body = r_post.json()
        self.__class__.role_id = self.role_body['id']
        self.assertEqual(201, r_post.status_code)

        r_get_item = requests.get(self.base_url + '/roles/' + str(self.__class__.role_id))
        self.role_body = r_get_item.json()
        self.role_data['id'] = self.__class__.role_id
        self.assertEqual(self.role_data, self.role_body)

        r_get_list = requests.get(self.base_url + '/roles')
        roles_list = r_get_list.json()
        for item in roles_list:
            if item['id'] == self.__class__.role_id:
                self.role_from_list = item
        self.assertEqual(self.role_data, self.role_from_list)

    def test2_put(self):
        self.role_data_new = {'name': 'Hero Changed', 'type': 'Supernatural', 'level': 6}

        r_put = requests.put(self.base_url + '/roles/' + str(self.__class__.role_id), self.role_data_new)
        self.assertEqual(200, r_put.status_code)

        r_get_item = requests.get(self.base_url + '/roles/' + str(self.__class__.role_id))
        self.role_body = r_get_item.json()
        self.role_data_new['id'] = self.__class__.role_id
        self.role_data_new['book'] = self.book_id
        self.assertEqual(self.role_data_new, self.role_body)

        r_get_list = requests.get(self.base_url + '/roles')
        roles_list = r_get_list.json()
        for item in roles_list:
            if item['id'] == self.__class__.role_id:
                self.role_from_list = item
        self.assertEqual(self.role_data_new, self.role_from_list)

    def test3_delete(self):
        r_del_item = requests.delete(self.base_url + '/roles/' + str(self.__class__.role_id))
        self.assertEqual(204, r_del_item.status_code)
        r_get_item = requests.get(self.base_url + '/roles/' + str(self.__class__.role_id))
        self.assertEqual(404, r_get_item.status_code)

    def tearDown(self):
        if self.book_id is not None:
            requests.delete(f'{self.base_url}/books/{self.book_id}')


if __name__ == '__main__':
    unittest.main()
