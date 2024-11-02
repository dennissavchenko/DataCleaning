from sklearn.preprocessing import StandardScaler


def normalize_numerical_data_z_score(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
