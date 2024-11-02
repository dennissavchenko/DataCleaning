import pandas as pd
from mongoDB import MongoDB
from data_standardization import *
from data_cleaning import *

df = pd.read_csv('usa_house_prices.csv')

#db = MongoDB('pro')

# Sending the uncleaned data to the database first
#db.insert_collection('house_prices_data_raw', df)

# Deleting 'country' column because its every value is 'USA' (not useful)
df = delete_columns(df, ['country', 'street'])

# Converting 'date' column into datatime ISO format (correcting datatype)
df = format_date_columns(df, ['date'])

# Filling missing values in the 'date' column with the next not null entry (as we see the data are sorted by date)
df = fill_missing_with_next_value(df, ['date'])

# Deletes entries with missing house prices
df = drop_missing_entries(df, ['price'])

# Filling missing values in the numerical columns with the mean
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df = fill_missing_with_mean(df, numeric_cols)

# Filling missing values in the categorical columns with 'unknown' (could also use removing)
categorical_cols = df.select_dtypes(include=['object']).columns
df = fill_missing_with_unknown(df, categorical_cols)

# Removing outliers (houses with extreme prices)
df = remove_outliers_iqr(df, ['price'])

# Removing duplicates
df = df.drop_duplicates()

# Printing every column's datatype to doublecheck their correctness
#print("Columns datatypes:\n", df.dtypes)

# Sending the cleaned data to the database
#db.insert_collection('house_prices_data_cleaned', df)

df = normalize_numerical_data_z_score(df,['price', 'bedrooms', 'bathrooms', 'sqft_living', 'floors', 'sqft_lot', 'sqft_above', 'yr_built', 'sqft_basement', 'yr_renovated'])
df, label_encoders = standardize_categorical_data(df, ['city'])
pd.set_option('display.max_columns', None)

print(df)


