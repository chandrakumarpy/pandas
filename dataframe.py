import pandas as pd
data = {
    "Car Name": ["Tata Punch", "Maruti Swift", "Hyundai i20", "Tata Nexon", 'Maruti Belano'],
    "Price": [1000000, 800000, None, 1200000, 1500000],
    "Mileage": [20, None, 18, 17, 15],
    "Fuel Type": ["Petrol", "Petrol", "Diesel", None, "Diesel"],
    "Transmission": ["Manual", "Manual", None, "Automatic", "Manual"]
}
df = pd.DataFrame(data)
print(df.shape)
print(df.info())
print(df.describe())
print(df.iloc[2:4])
print(df.iloc[2:4, 0:2])
print(df.loc[2:3, ["Car Name","Price"]])
df.drop("Fuel Type", axis = 1, inplace = True) # this change the original values normal time inplace = False always
df["Mileage"] = df["Mileage"] + 5 # broad cast increase the values
df.rename(columns = {'Car Name':'indian_car'}, inplace = True)
print(df)

# null values and drop null values

# print(df.isnull().sum())
# print(df.dropna())
# print(df.dropna(axis=1))
# print(df.dropna(subset=["Price"]))
rows_all_null = df[df.isnull().any(axis=1)]
print(rows_all_null)
# axis=1 → row-wise
# .any() → at least one null
# .all() → all null
# .sum() → count of nulls

# add fill values 
df["Mileage"] = df["Mileage"].apply(lambda x : df["Mileage"].mean() if pd.isnull(x) else x)
df["Price"].fillna(df["Price"].mean(), inplace= True)
df.fillna(method = 'ffill', inplace= True) # for back values add 'bfill'

# pandas merge

import pandas as pd
customers = {
    "customer_id": [1, 2, 3, 4],
    "customer_name": ["Amit", "Ravi", "Sita", "John"]
}
orders = {
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 2, 5],  # notice 5 (no match)
    "amount": [500, 700, 300, 900]
}
df1 = pd.DataFrame(customers)
# df1.set_index("customer_id", inplace=True)
df2 = pd.DataFrame(orders)
# df2.set_index("customer_id", inplace=True)

# df = pd.merge(df1, df2, on ="customer_id", how = 'left')
# df = df1.join(df2, how = "inner")
df = pd.concat([df1, df2], axis = 1)
print(df)
