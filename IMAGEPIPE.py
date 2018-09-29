# coding=utf-8
import os
import requests
from SETTINGS import IMAGE_STORE

class ImagePipeLine():

    def download(self,data):
        if not os.path.exists(IMAGE_STORE):
            os.mkdir(IMAGE_STORE)
        try:
            response = requests.get(url=data['Image'])
            if response.status_code == 200:
                file_path = '{}/{}.{}'.format(IMAGE_STORE,data['User'].replace(' ',''),'jpg')
                if not os.path.exists(file_path):
                    with open(file_path,'wb') as f:
                        f.write(response.content)
                    print('{} Download Successfully!'.format(data['User']))
                else:
                    print('{} Already download'.format(data['User']))
        except requests.ConnectionError as e:
            print('Failed to save image')


