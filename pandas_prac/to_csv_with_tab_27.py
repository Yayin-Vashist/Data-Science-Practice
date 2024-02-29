import numpy as np
import pandas as pd

data = {"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]}

df = pd.DataFrame(data)

df.to_csv("./../csv/pandas_prac_27.csv", sep="\t", index=False)
new_df = pd.read_csv("./../csv/pandas_prac_27.csv")

print(df)
print("\n" + "-" * 30)
print(new_df)
