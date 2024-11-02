import os
from pymongo.mongo_client import MongoClient


class MongoDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = self.connect_to_mongodb()

    def connect_to_mongodb(self):
        try:
            client = MongoClient(os.getenv('MONGODB_URI'))
            db = client[self.db_name]
            print(f"Connected to MongoDB database '{self.db_name}'")
            return db
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return None

    # Takes collection name and DataFrame and creates a new dataset in the database using the data
    def insert_collection(self, collection_name, data):
        collection = self.db[collection_name]
        data_dict = data.to_dict(orient='records')
        try:
            collection.insert_many(data_dict)
            print(f"Data successfully inserted into MongoDB collection '{collection_name}'!")
        except Exception as e:
            print(f"An error occurred while inserting data: {e}")
