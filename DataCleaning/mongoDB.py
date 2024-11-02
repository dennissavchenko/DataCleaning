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

    # Clears collection and inserts given data frame
    def reset_collection_and_insert(self, collection_name, df):
        self.clear_collection(collection_name)
        self.insert_collection(collection_name, df)

    # Inserts given data frame to specified collection
    def insert_collection(self, collection_name, df):
        collection = self.db[collection_name]
        data_dict = df.to_dict(orient='records')
        try:
            collection.insert_many(data_dict)
            print(f"Data successfully inserted into MongoDB collection '{collection_name}'!")
        except Exception as e:
            print(f"An error occurred while inserting data: {e}")

    # Clears all documents in a specified collection
    def clear_collection(self, collection_name):
        collection = self.db[collection_name]
        try:
            result = collection.delete_many({})
            print(f"Cleared {result.deleted_count} documents from '{collection_name}' collection.")
        except Exception as e:
            print(f"An error occurred while clearing the collection: {e}")

    # Updates documents in a collection based on a filter
    def update_documents(self, collection_name, filter_query, update_data):
        collection = self.db[collection_name]
        try:
            result = collection.update_many(filter_query, {'$set': update_data})
            print(f"Updated {result.modified_count} documents in '{collection_name}' collection.")
        except Exception as e:
            print(f"An error occurred while updating documents: {e}")

    # Inserts a single document into a collection
    def insert_single_document(self, collection_name, document):
        collection = self.db[collection_name]
        try:
            collection.insert_one(document)
            print(f"Document successfully inserted into '{collection_name}' collection!")
        except Exception as e:
            print(f"An error occurred while inserting the document: {e}")

    # Deletes documents in a collection based on a filter
    def delete_documents(self, collection_name, filter_query):
        collection = self.db[collection_name]
        try:
            result = collection.delete_many(filter_query)
            print(f"Deleted {result.deleted_count} documents from '{collection_name}' collection.")
        except Exception as e:
            print(f"An error occurred while deleting documents: {e}")
