# coding=utf-8

import pymongo
import SETTINGS

class MongoPipeLine():

    def __init__(self):
        self.client = pymongo.MongoClient(SETTINGS.MONGO_URI,connect=False)
        self.db = self.client[SETTINGS.MONGO_DB]
        self.collection = SETTINGS.COLLECTION

    def insert(self,data):
        if self.db[self.collection].find_one(data):
            print('Data has been existed')
        else:
            self.db[self.collection].insert(data)
            print('Insert Successfully!')

    def close(self):
        self.client.close()