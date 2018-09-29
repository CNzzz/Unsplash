#utf8
from urllib.parse import urlencode
import requests

class Spider():
    base_url = 'https://unsplash.com/napi/photos?'

    def get_page(self,page):
        params = {
        'page':page,
        'per_page':12,
        'order_by':'latest'
        }
        #动态构建请求
        url = self.base_url + urlencode(params)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError as e:
            print('Error',e.args)

    def parse(self,json):
        if json:
            for item in json:
                data = {}
                data['User'] = item.get('user').get('name')
                data['Location'] = item.get('user').get('location')
                data['Host'] = item.get('user').get('portfolio_url')
                data['Image']=item.get('urls').get('full')
                data['Likes'] = item.get('user').get('total_likes')
                yield data


