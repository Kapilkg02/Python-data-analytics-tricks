import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")
#rename colmuns  ,  note in remaning {} braket works
new1 = new_data.rename(columns ={'Sales_in_thousands': "sales", '__year_resale_value': "year" })
new1.columns
# similar command is of  droping variable but with [] brakets
drop_data = new_data.drop(columns=["Price_in_thousands", 'Curb_weight', 'Fuel_capacity'])

#sum , mean, std, and others
sum1 = new1[["sales","year"]].sum()
sum1
#number of rows in variable
new1.sales.count()