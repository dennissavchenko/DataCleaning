# Deletes specified columns from given data frame
def delete_columns(df, columns):
    df = df.drop(columns=columns)
    return df


# Filling missing values in specified columns with the next not null entry
def fill_missing_with_next_value(df, columns):
    df[columns] = df[columns].bfill()
    return df


# Deletes entries if values of specified columns are missing
def drop_missing_entries(df, columns):
    df.dropna(subset=columns, inplace=True)
    return df


# Filling missing values in the specified numerical columns with the mean
def fill_missing_with_mean(df, columns):
    df[columns] = df[columns].fillna(df[columns].mean())
    return df


# Filling missing values in the specified categorical columns with 'unknown'
def fill_missing_with_unknown(df, columns):
    df[columns] = df[columns].fillna('unknown')
    return df


# Removes outliers from the specified columns of the using the IQR method.
def remove_outliers_iqr(df, columns):
    for column in columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df
