import pandas as pd
s= pd.Series([i for i in range(100, 1000,100)])
index = ['a','b','c','d','e','f','g', 'h','i']
s.index = index
s.name = 'my_numbers'
print(s['a':'f'])
print(s.iloc[8]) # index based
print(s.iloc[[1,4,6]])
print(s.loc['f']) # labled bsed
# ---------------------------------
import pandas as pd
cars = {
    "Tata Punch": 1000000,
    "Maruti Swift": 800000,
    "Hyundai i20": 900000,
    "Tata Nexon": 1200000,
    "Mahindra Thar": 1500000,
    "Kia Seltos": 1400000,
    "Toyota Fortuner": 3500000,
    "Honda City": 1300000,
    "Skoda Slavia": 1200000,
    "Volkswagen Virtus": 1300000
}
s= pd.Series(cars, name = 'cars')
# print(s>1000000)
print(s[s>=1000000])
print(s[(s>=1000000) & (s<=1500000)])
print(s[~(s>=1000000)])
s["Hyundai i20"] = 1200000
print(s)