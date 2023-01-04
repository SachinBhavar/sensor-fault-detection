import pymongo
from sensor.constant.database import DATABASE_NAME
#from sensor.constant.env_variable import MONGODB_URI_KEY
import certifi
import os
ca=certifi.where()

class MongoDBClient:
    client=None
    def __init__(self,database_name=DATABASE_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url= "mongodb+srv://sachinbhavar:sachswara@cluster0.14heklc.mongodb.net/?retryWrites=true&w=majority"
                if "localhost" in mongo_db_url:
                    MongoDBClient.client=pymongo.MongoCLient(mongo_db_url,tlsCAFile=ca)
            self.client=MongoDBClient.client
            self.database=self.client[database_name]
            self.database_name=database_name
        except Exception as e:
            raise e
        

