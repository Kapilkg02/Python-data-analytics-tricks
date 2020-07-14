# importing dataset in sheet car
import pandas as pd

new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")
# head and tail of dataset
data_head = new_data.head(50)
data_tail = new_data.tail(50)

# contents and row colums, count
new_data.dtypes
new_data.columns
new_data.count()
new_data.shape
rows, columns = new_data.shape
rows
columns
