from pymongo import MongoClient
from app.config import config as cfg


class Connection:

    HOST = None
    PORT = None
    USER_NAME = None
    PASSWORD = None
    DB_NAME = None
    CONNECTION = False
    _DB = None

    def __init__(self):
        self.HOST = cfg.get("mongo", "HOST")
        self.PORT = cfg.get("mongo", "PORT")
        self.USER_NAME = cfg.get("mongo", "USER_NAME")
        self.PASSWORD = cfg.get("mongo", "PASSWORD")
        self.DB_NAME = cfg.get("mongo", "DB_NAME")

    def get_db(self):
        if not self.CONNECTION:
            client = MongoClient(
                f"mongodb://{self.USER_NAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}"
            )
            self._DB = client[self.DB_NAME]
            self.CONNECTION = True
        return self._DB

    def get_collections(self):
        qmul = self.get_db()
        qmul.list_collection_names()

    def get_jobs(self, keywords):
        qmul = self.get_db()
        collection = qmul["jobs"]
        args = []
        # for keyword in keywords:
        #     args.append({ 'keywords' : { '$regex' : '.*' + keyword + '.*', '$options' : 'i' } } )
        return collection.find()[0:10]

        #return collection.find({ '_keywords' : { '$regex' : '.*' + keywords + '.*', '$options' : 'i'}})

    def push_jobs(self, jobs: list):
        qmul = self.get_db()
        collection = qmul["jobs"]
        for job in jobs:
            try:
                dict = job.__dict__
                dict['_company_name'] = job.company.name
                dict['_company_website'] = job.company.website
                collection.insert_one(dict)
            except:
                print('exception ignored')

        return None


mongo_db = Connection()
