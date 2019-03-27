import requests


def post_item(base_url, part_url, data):
    r_post_item = requests.post(base_url+part_url, data)
    role = r_post_item.json()
    return r_post_item, role['id']


def get_item(role_id, base_url, part_url):
    r_get_item = requests.get(base_url+part_url+'/'+str(role_id))
    return r_get_item.json()


def get_list(base_url, part_url):
    r_get_list = requests.get(base_url+part_url)
    return r_get_list.json()


def put_fields(role_id, base_url, part_url, data_new):
    r_put = requests.put(base_url+part_url+'/'+str(role_id), data)
    return r_put


def del_item(role_id, base_url, part_url):
    r_del_item = requests.delete(base_url+part_url+'/'+str(role_id))
    return r_del_item


if __name__ == "__main__":
    base_url = 'http://pulse-rest-testing.herokuapp.com'
    part_url = '/roles'
    data = {'name': 'Hero 1', 'type': 'Supernatural', 'level': 5, 'book': 104}
    data_new = {'name': 'Hero Changed', 'level': 6}

    r_post_item, role_id = post_item(base_url, part_url, data)
    print(role_id)

    p = put_fields(role_id, base_url, part_url)
    print(p)

    d = del_item(role_id, base_url, part_url)
    print(d)
