from django.test import TestCase

# Create your tests here.
add_url = '/pre/add/'
del_url = '/pre/delete/'
content_type = 'application/json'
change_url = '/pre/edit/'
search_url = '/pre/query?'


class Test(TestCase):
    def setUp(self):
        pass

    def add(self, body):
        return self.client.post(add_url, data=body, content_type=content_type)

    def test_add(self):
        # return
        body = {
            'date': '2021-5-31',
            'home_name': 'wangzhitong',
            'away_name': 'haha',
            'home_score': 100,
            'away_score': 50,
            'tournament': 'FIFA World Cup',
            'league_mark': 0
        }
        response = self.add(body)
        self.assertJSONEqual(response.content, {
            'code': 200,
            'data': {'message': 'add successfully!'}
        })

    def delete_data(self):
        return self.client.get(del_url)

    def test_del(self):
        body = {
            'date': '2021-5-31',
            'home_name': 'china',
            'away_name': 'japan',
            'home_score': 100,
            'away_score': 50,
            'tournament': 'FIFA World Cup'
        }
        self.add(body)
        response = self.delete_data()
        self.assertEqual(response.status_code, 200)

    def change(self, body):
        return self.client.post(change_url, data=body, content_type=content_type)

    def test_change(self):
        self.delete_data()
        body = {
            'date': '2021-5-31',
            'home_name': 'testchange',
            'away_name': 'japan',
            'home_score': 100,
            'away_score': 50,
            'tournament': 'FIFA World Cup'
        }
        result = self.change(body)
        self.assertEqual(result.status_code, 200)

    def search(self, getUrl):
        return self.client.get(search_url + getUrl)

    def test_search(self):
        body = {
            'date1': '2016-09-01',
            'date2': '2018-10-01',
            'name': 'spain',
            'tournament': 'Friendly',
            'result': 1.0
        }
        getUrl = '?tournament=' + body['tournament'] + '&name=' + body['name'] + '&date1=' + body['date1'] \
                 + '&date2=' + body['date2'] + '&result=' + str(body['result'])
        response = self.search(getUrl)
        print(response.content)
