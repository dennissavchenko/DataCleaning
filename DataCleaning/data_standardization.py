from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd


def normalize_numerical_data_z_score(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df


def standardize_categorical_data(df, columns):
    label_encoders = {}
    for column in columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column].astype(str))
        label_encoders[column] = le
    return df, label_encoders


def format_date_columns(df, date_columns, date_format='%Y-%m-%d'):
    for column in date_columns:
        # In case of invalid date format value, it will be replaced by NaT
        df[column] = pd.to_datetime(df[column], errors='coerce')
        df[column] = df[column].dt.strftime(date_format)
    return df
