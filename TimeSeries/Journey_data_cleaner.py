import pandas as pd 

FilePath= input('Enter File Path ? ')

data = pd.read_csv(FilePath)
print("Data Reading completed .....")

train_data = data
print(f"Unique users in the given data :::: {len(train_data['user_id'].unique())}")
print(f"Unique number of sessions in given data ::::: {len(train_data['user_session'].unique())}")

train_data = train_data.drop(["product_id", "category_id", "category_code", "brand", "price"], axis=1)

grouped_data = train_data.sort_values(by=["user_id", "user_session", "event_time"]).reset_index(drop=True)
grouped_data

grouped_df____ = grouped_data.groupby(['user_id', 'user_session']).agg({'event_type': lambda x:list(x)}).reset_index()

grouped_df____["event_type"] = grouped_df____["event_type"].apply(lambda x: ", ".join(x))
print(f"Total number of userid after grouping ::: {grouped_df____['user_id'].nunique()}")

while True:

    print(grouped_df____["user_id"].value_counts().sort_values(ascending=False).head(20))

    ID = int(input('Enter any id in the above 20 user_ids ? '))

    User_spec_df = grouped_df____[grouped_df____["user_id"] == ID].reset_index(drop=True)

    print(User_spec_df["event_type"].unique().tolist())

    