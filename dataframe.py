import pandas as pd
data = {
    "Car Name": ["Tata Punch", "Maruti Swift", "Hyundai i20", "Tata Nexon", 'Maruti Belano'],
    "Price": [1000000, 800000, None, 1200000, 1500000],
    "Mileage": [20, None, 18, 17, 15],
    "Fuel Type": ["Petrol", "Petrol", "Diesel", None, "Diesel"],
    "Transmission": ["Manual", "Manual", None, "Automatic", "Manual"]
}
df = pd.DataFrame(data)
print(df.iloc[2:4])
print(df.iloc[2:4, 0:2])
print(df.loc[2:3, ["Car Name","Price"]])
df.drop("Fuel Type", axis = 1, inplace = True) # this change the original values normal time inplace = False always
df["Mileage"] = df["Mileage"] + 5 # broad cast increase the values
df.rename(columns = {'Car Name':'indian_car'}, inplace = True)
print(df)