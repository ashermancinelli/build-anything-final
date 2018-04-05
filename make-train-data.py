import pandas as pd
import numpy as np
import sklearn


col_names = ['year', 'rank', 'w', 'win_pct', 'fp', 'bpf', 'ppf']
df = pd.read_pickle('train-merged.pkl')

df = df[[i + '1' for i in col_names]]
temp = df.sample(frac=1).reset_index(drop=True)

for i in col_names:
	df[i + '2'] = temp[i + '1']

for i in col_names:
	df[i + '_diff'] = df[i + '1'] - df[i + '2']

def to_binary(row):
	if row['win_pct_diff'] > 0:
		return 1
	elif row['win_pct_diff'] < 0:
		return -1
	else:
		return -1

	

df['label'] = df.apply(to_binary, axis=1)

df.to_pickle('train-data-final.pkl')

print(df.head())




