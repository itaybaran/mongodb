from pymongo import MongoClient


class data_mongo:
    def __init__(self,config,logger):
        self.config = config.get_config()
        self.logger = logger
        self.mongo_con_str = self.config.get_config()["mongo_config"]["con_str"]
        self.mongo_db_name = self.config.get_config()["mongo_config"]["db_name"]
        self.mongo_collection_name = self.config.get_config()["mongo_config"]["collection_name"]
        self.db = self.get_db()
        self.collection = self.db[self.mongo_collection_name]

    def get_db(self):
        client = MongoClient(self.mongo_con_str)
        # Create the database for our example (we will use the same database throughout the tutorial
        return client[self.mongo_db_name]

    def get_doc_by_id(self,_id):
        return self.collection.find_one({"_id": _id})