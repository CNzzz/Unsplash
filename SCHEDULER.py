# coding=utf-8
from IMAGEPIPE import ImagePipeLine
from SPIDER import Spider
from MONGOPIPE import MongoPipeLine
from multiprocessing import Pool

spider = Spider()
mongo = MongoPipeLine()
image = ImagePipeLine()

def run(i):
    for page in range(i,i+20):
        response = spider.get_page(page)
        data_list = spider.parse(response)
        for data in data_list:
            mongo.insert(data)
            image.download(data)

if __name__ == '__main__':
    pool = Pool(20)
    pool.map(run,[i*20 for i in range(10)])
    pool.close()
    pool.join()
    mongo.close()