def transform_posts(df):
    
    if df.isnull().sum().sum() > 0:
        raise ValueError("Null values detected in data")

    if not {"userId", "id", "title", "body"}.issubset(df.columns):
        raise ValueError("Missing required columns")

    df["title"] = df["title"].str.strip()
    df["body"] = df["body"].str.strip()

    return df