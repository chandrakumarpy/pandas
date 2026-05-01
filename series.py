import pandas as pd
s= pd.Series([i for i in range(100, 1000,100)])
index = ['a','b','c','d','e','f','g', 'h','i']
s.index = index
s.name = 'my_numbers'
print(s['a':'f'])
print(s.iloc[8]) # index based
print(s.iloc[[1,4,6]])
print(s.loc['f']) # labled bsed
