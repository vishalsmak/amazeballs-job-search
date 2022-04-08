from app.config import config as cfg
import urllib.parse
import pymongo


class Connection:
    HOST = None
    PORT = None
    USER_NAME = None
    PASSWORD = None
    DB_NAME = None
    _CLIENT = None

    def __init__(self):
        self.HOST = cfg.get("mongo", "HOST")
        self.PORT = cfg.get("mongo", "PORT")
        self.USER_NAME = cfg.get("mongo", "USER_NAME")
        self.PASSWORD = cfg.get("mongo", "PASSWORD")
        self.DB_NAME = cfg.get("mongo", "DB_NAME")

    def get_client(self):
        if not self._CLIENT:
            self._CLIENT = pymongo.MongoClient(f'mongodb://{self.USER_NAME}:{urllib.parse.quote_plus(self.PASSWORD)}@{self.HOST}:{self.PORT}/{self.DB_NAME}')
        return self._CLIENT

    def get_collections(self):
        qmul = self.get_client().qmul
        qmul.list_collection_names()

    def get_jobs(self):
        qmul = self.get_client().qmul
        data = qmul.jobs
        return data

    def push_jobs(self, jobs):
        qmul = self.get_client().qmul
        collection = qmul.jobs
        collection.insert_many(jobs)
        return


mongo_db = Connection()

