from pymongo import MongoClient
from dotenv import load_dotenv
import os


class Database:
    @staticmethod
    def _connect():
        try:
            CONNECTION_STRING =f"mongodb://{os.environ.get("IP")}:{os.environ.get("PORT")}"
            print("conexão com o mongo")
            print(CONNECTION_STRING)
            
            connection = MongoClient(CONNECTION_STRING)
            return connection
        except Exception as e:
            print(e)

    @staticmethod 
    def _close(connection):
        try:
            connection.close()
        except Exception as e:
            print(e)

    @staticmethod
    def _get_collection(collection_name, DB_NAME):
        try:
            connection = Database()._connect()
            database_ = connection[DB_NAME]
            collection = database_[collection_name]

            return collection, connection       
        except Exception as e:
            print(e)

    @staticmethod
    def _insert_one(query, collection_name, DB_NAME = os.environ.get("DB_NAME")):
        try:
            collection, connection = Database()._get_collection(collection_name, DB_NAME)
            result = collection.insert_one(query)

            Database()._close(connection)
            return result
        except Exception as e:
            print(e)

    @staticmethod
    def _delete_one(query, collection_name, DB_NAME = os.environ.get("DB_NAME")):
        try:
            collection, connection = Database()._get_collection(collection_name, DB_NAME)
            result = collection.delete_one(query)

            Database()._close(connection)
            return result
        except Exception as e:
            print(e)

    @staticmethod
    def _find_one(query, collection_name, DB_NAME = os.environ.get("DB_NAME")):
        try:
            collection, connection = Database()._get_collection(collection_name, DB_NAME)
            result = collection.find_one(query)

            Database()._close(connection)
            return result
        except Exception as e:
            print(e)

    @staticmethod
    def _update_one(query, document, collection_name, DB_NAME = os.environ.get("DB_NAME")):
        try:
            collection, connection = Database()._get_collection(collection_name, DB_NAME)
            result = collection.update_one(query, {"$set":document})

            Database()._close(connection)
            return result
        except Exception as e:
            print(e)
    
    @staticmethod
    def _find_all(query, collection_name, DB_NAME = os.environ.get("DB_NAME")):
        try:
            collection, connection = Database()._get_collection(collection_name, DB_NAME)
            result = list(collection.find(query))

            Database()._close(connection)
            return result
        except Exception as e:
            print(e)
