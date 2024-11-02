import pandas as pd
from mongoDB import MongoDB
from data_standardization import *

df = pd.read_csv('usa_house_prices.csv')

#db = MongoDB('pro')

# Sending the uncleaned data to the database first
#db.insert_collection('house_prices_data_raw', df)

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

# Removing duplicates
df = df.drop_duplicates()

# Printing every column's datatype to doublecheck their correctness
#print("Columns datatypes:\n", df.dtypes)

# Sending the cleaned data to the database
#db.insert_collection('house_prices_data_cleaned', df)

df = normalize_numerical_data_z_score(df,['price', 'bedrooms', 'bathrooms', 'sqft_living', 'floors', 'sqft_lot', 'sqft_above', 'yr_built'])
pd.set_option('display.max_columns', None)
print(df)


