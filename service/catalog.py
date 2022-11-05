from sqlalchemy import create_engine
from urllib import parse
import datetime
import pandas as pd
import uuid
import json

class Catalog:
    def __init__(self,config,logger):
        self.config = config.get_config()
        self._con_str = self.config["db_config"]["con_str"]
        params = parse.quote_plus(self._con_str) # Like quote(), but also replace spaces with plus signs, as required for quoting HTML form values when building up a query string to
                                                 # go into a URL. Plus signs in the original string are escaped unless they are included in safe. It also does not have safe default to '/'.
                                                 # Example: quote_plus('/El Niño/') yields '%2FEl+Ni%C3%B1o%2F'.
        self.engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params)) # The Engine is the starting point for any SQLAlchemy application.
                                                                                       # It’s “home base” for the actual database and its DBAPI,
                                                                                       # delivered to the SQLAlchemy application through a connection pool and a Dialect,
                                                                                       # which describes how to talk to a specific kind of database/DBAPI combination.
        self.logger = logger

    def save_data(self,dict_attributes):
        key = str(uuid.uuid4())
        user = str(self.get_user())
        ts = datetime.datetime.today()
        action = "I"
        attrib = json.dumps(dict_attributes)
        data = {'obj_key': [key],
                'action_type': [action],
                'action_ts': [ts],
                'user_name': [user],
                'attributes':[attrib]}

        # create dataframe
        df = pd.DataFrame(data)
        self.logger.logger.info(data)
        df.to_sql(             #Write records stored in a DataFrame to a SQL database.
            'log',             #if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
                               # How to behave if the table already exists.
            self.engine,       #indexbool, default True
                               # Write DataFrame index as a column. Uses index_label as the column name in the table.
            if_exists='append',
            index=False
        )

    def load_data(self,query_str):
        return pd.read_sql(
            query_str,
            con=self.engine,
            parse_dates=[])

    def get_user(self):
        return pd.read_sql(
            "select SYSTEM_USER",
            con=self.engine)