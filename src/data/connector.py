from pymongo import MongoClient
from app.config import config as cfg
from src.Entities.Job import Job

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

    #TODO : Get jobs from mongo
    def get_jobs(self, keywords: list[str]) -> list[Job]:
        qmul = self.get_db()
        collection = qmul["jobs"]
        args = []
        for keyword in keywords:
            args.append({ 'keywords' : { '$regex' : '.*' + keyword + '.*', '$options' : 'i' } } )
        return collection.find(*args) 

    def push_jobs(self, jobs: list[Job]):
        qmul = self.get_db()
        collection = qmul["jobs"]
        for job in jobs:
            collection.insert_one(job.__dict__)
        return

mongo_db = Connection()
