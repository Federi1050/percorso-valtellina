import pandas as pd

s = pd.Series([1,2,3,4,5,6], index=['a','b','c','d','e','f'])

print(s['e'])
print(s[['a','f']])

data = {
    'Nome' : ['Luca', 'Mario'],
    'Eta' : [10,12],
    'Citta' : ['Roma', 'Milano']
}

df = pd.DataFrame(data)
print(df)