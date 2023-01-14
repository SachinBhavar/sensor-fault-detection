from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys

def testException():
    try:
        x=1/0
        testException()
    except Exception as e:
        raise SensorException(e,sys)


if __name__=='__main__':
    try:
        testException()
    except Exception as e:
        print(e)

    Mongodb_Client=MongoDBClient()
    print("collection.name:",Mongodb_Client.database.list_collection_names())