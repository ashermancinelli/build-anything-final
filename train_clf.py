from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd

df = pd.read_pickle('train-data-final.pkl')
col_names = ['year', 'rank', 'w', 'win_pct', 'fp', 'bpf', 'ppf']

x = df[['year_diff', 'rank_diff', 'w_diff', 'fp_diff', 'bpf_diff', 'ppf_diff']]

y = df['label']

clf = RandomForestClassifier(n_estimators=100)
clf = clf.fit(x, y)

pickle.dump(clf, open('clf.pkl', 'wb'))

