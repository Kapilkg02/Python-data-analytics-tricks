

import pandas as pd
#replace
sale = pd.read_excel("D:\Car_sales.xlsx", sheet_name = "sale" )
sale
#dictionary
re = {"Sales_in_thousands":-99999 ,"__year_resale_value": [-77777,13.360] ,"Engine_size": [-999999, 0.854]}
import numpy as np
sale1 = sale.replace(re,np.NaN) # repalcinv with missing (NaN)
sale1 = sale.replace(re,0) # relacing with 0

# multpile replace with char and number
sale1 =sale.replace({-99999 : np.NaN, "BMW" : "SUW" ,-999999 : 10 })
# or can be done in this way also
sale1 =sale.replace([-99999  ,"BMW" ,-999999],[np.NaN, "SUW" , 10 ])
sale1