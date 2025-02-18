import pandas as pd

data = pd.read_csv('netflix_titles.csv')
data.drop_duplicates(inplace=True)
data.dropna(subset=['director', 'country', 'date_added'], inplace=True)
data['date_added'] = pd.to_datetime(data['date_added'])
