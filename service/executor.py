import os
from service.mongo import data_mongo
from service.configuration import Config
from service.logger import Logger
from service.files_manip import Files_manip
import datetime, sys


class Executor:
    def __init__(self, config_file_path):
        self.config = Config(config_file_path)
        self.logger = Logger(self.config)
        self.logger.set_logger()
        self.mongo = data_mongo(self.config,self.logger)

    def get_document_by_id(self,id_):
        item = self.mongo.get_doc_by_id(id_)