import pandas as pd

a = pd.read_excel('cfg_test.xlsx')

a['Salary'] = a['Salary'].str.strip('$')
a['Salary'] = a['Salary'].str.replace(',', '')

a.to_excel('test.xlsx')

