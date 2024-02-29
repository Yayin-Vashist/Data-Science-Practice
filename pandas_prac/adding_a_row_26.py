import numpy as np
import pandas as pd

data = {"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]}

df = pd.DataFrame(data)

print(df)
df = df._append({"col1": 1, "col2": 8, "col3": 5}, ignore_index=True)

print("-" * 30)

print(df)
