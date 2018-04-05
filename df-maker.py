import sqlite3
import pandas
import numpy
import pickle

db = sqlite3.connect('data/database.sqlite')
df = pandas.read_sql('select * from team;', db)
df.to_pickle('team-df.pkl')


