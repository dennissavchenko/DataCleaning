import pandas as pd
import os
from pymongo.mongo_client import MongoClient

df = pd.read_csv('usa_house_prices.csv')

# Connecting to MongoDB
client = MongoClient(os.getenv('MONGODB_URI'))
db = client['pro']


# Takes collection name and data frame and creates new dataset in the database using the data
def insert_collection(collection_name, data):
    collection = db[collection_name]
    data_dict = data.to_dict(orient='records')
    try:
        collection.insert_many(data_dict)
        print("Data successfully inserted into MongoDB!")
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")


# Sending the uncleaned data to the database first
insert_collection('house_prices_data_raw', df)
