import pandas as pd

df = pd.read_csv(r'data\hacker_news.csv')

first_5_rows = df.head()


last_5_rows = df.tail()


title_series = df.iloc[:,2]


python_title = df.loc[df['title'].str.contains('Python', case=False)]


js_title = df.loc[df['title'].str.contains('JavaScript', case=False)]
