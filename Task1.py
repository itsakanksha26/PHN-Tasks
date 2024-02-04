import pandas as pd
car_sp = pd.DataFrame({
    'Company Name': ['Hyundai', 'Honda', 'KIA'],
    'Model Name': ['Creta', 'Civic', 'Seltos'],
    'Fuel Type': ['Diesel', 'Petrol', 'Diesel'],
    'Body Style': ['SUV', 'Sedan', 'SUV'],
    'Car Length': ['4300', '4557', '4315'],
})
car_sp.to_csv('car_sp.csv', index=False)
car_pricing = pd.DataFrame({
    'Company Name': ['Hyundai', 'Honda', 'KIA'],
    'Model Name': ['Creta', 'Civic', 'Seltos'],
    'On Road Pricing': [1598000, 2103000, 969000],
    'Loan Amt': [1000000, 1500000, 500000],
    'Monthly EMI': [16879, 25319, 8440],
    'Interest Rate': [0.5, 0.5, 0.5],
    'Monthly Principal': [12367, 18551, 6184],
    'Monthly Interest': [292, 438, 145],
})
car_pricing.to_excel('car_pricing.xlsx', index=False),
car_sp_df =pd.read_csv('car_sp.csv')
car_pricing_df =pd.read_excel('car_pricing.xlsx'),
merged_df =pd.merge(car_sp_df, car_pricing_df, on=['Company Name', 'Model Name'])
merged_df.fillna(0, inplace=True)
gst_rate =0.18
merged_df['On Road Pricing'] =merged_df['On Road Pricing'] +merged_df['On Road Pricing']*gst_rate
print(merged_df)