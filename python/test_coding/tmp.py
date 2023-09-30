import pandas as pd

data = pd.read_csv('Nowcoder.csv')
print(data.iloc[-5:][['Nowcoder_ID', 'Level', 'Achievement_value', 'Language']])