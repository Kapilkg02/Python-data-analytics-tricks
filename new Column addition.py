import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

# adding a new column and arthmatic operation
n2 = new_data
n2["discount"] = .05
n2["total_discount"] =n2.Sales_in_thousands * n2.discount
n3 = n2[["Manufacturer","Sales_in_thousands","discount","total_discount"]]
# or can be done in this way

n3 = new_data[["Manufacturer","Sales_in_thousands"]].head(10)

n3["dist"] = n3["Sales_in_thousands"]/100
n3
