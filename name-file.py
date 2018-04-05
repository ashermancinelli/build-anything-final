
import sqlite3
import pandas

db = sqlite3.connect('data/database.sqlite')
c = db.cursor()
data = pandas.read_sql('select name from team;', db)
names = set()
for i in data['name']:
	names.add(i)	
with open('names', 'w') as f:
	for i in names:
		f.write(i)
		f.write('\n')

