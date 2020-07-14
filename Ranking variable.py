import pandas as pd
loan = pd.read_csv("E:\Test 1.csv")
loan.head(2)
loan.dtypes
#ranking
df1 = loan
df1["rank"] = df1["imp_cscore"].rank(method="dense",ascending = False).astype(int)
df1[["imp_cscore", 'rank']]

df2 = df1.sort_values(["rank"] ,ascending = False)
df2 = df2.groupby("rank")["imp_cscore"].count()
df2

df2.rank()