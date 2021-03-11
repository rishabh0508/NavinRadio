from pymongo import MongoClient

import datetime
class In:
    def __init__(self, dbb, tbb):
            self.mCilent = MongoClient()
            self.db = self.mCilent[dbb]
            self.tb = self.db[tbb]

    def insert(self, data):
        self.tb.insert_many(data)

    def ad(self, id, x):
        self.tb.update_one(id, {"$inc": {"quantity": x}})


    def replace(self, id, x):
        self.tb.update_one(id, {"$set" : {"quantity": x}})

    def display(self):
        data = self.tb.find()
        return data

    def dis(self, da):
        data = self.tb.find(da)
        return data

    def de(self, d):
        self.tb.delete_one(d)

