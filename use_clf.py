import pandas as pd
import pickle

clf = pickle.load(open('clf.pkl', 'rb'))
df = pd.read_pickle('team-df.pkl')
col_names = ['year', 'rank', 'w', 'fp', 'bpf', 'ppf']

def run_clf(name1, year1, name2, year2):
	team1 = df[(df['name'] == name1) & (df['year'] == year1)]		
	team2 = df[(df['name'] == name2) & (df['year'] == year2)]		

	feed = []
	
	team1['win_pct'] = (team1['w'] / ( team1['w'] + team1['l'] ) )
	team2['win_pct'] = (team2['w'] / ( team2['w'] + team2['l'] ) )

	for i in col_names:
		feed.append(team1[i].values.tolist()[0] - team2[i].values.tolist()[0])

	result = clf.predict([feed])
	
	if result == 1:
		return name1
	else:
		return name2	

print(run_clf('Seattle Mariners', 2001, 'Chicago Cubs', 2015))
	
