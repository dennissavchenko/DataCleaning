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

# Deleting 'country' column because its every value is 'USA' (not useful)
df = df.drop(columns=['country'])

# Converting 'date' column into datatime format (correcting datatype)
df['date'] = pd.to_datetime(df['date'])

# Filling missing values in the 'date' column with the next not null entry (as we see the data are sorted by date)
df['date'] = df['date'].bfill()

# Deletes entries with missing house prices
df.dropna(subset=['price'], inplace=True)

# Filling missing values in the numerical columns with the mean
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Filling missing values in the categorical columns with 'unknown' (could also use removing)
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna('unknown')

# Removing outliers (houses with extreme prices)
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]


