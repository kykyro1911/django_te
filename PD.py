import pandas as pd
import sqlite3
from sqlalchemy import create_engine  
import sqlalchemy


engine = create_engine('sqlite:///db.sqlite3')
a = pd.read_csv('test.csv')
# conn = sqlite3.connect('db.sqlite3')


b=a.to_sql('ex_excel', engine, index=False, if_exists='append')

