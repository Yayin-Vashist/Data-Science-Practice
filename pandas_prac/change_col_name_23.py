import pandas as pd
import numpy as np

df = {"col1": [0, 1, 4, 7], "col2": [1, 2, 5, 8], "col3": [2, 3, 6, 9]}

df = pd.DataFrame(df)

print(df)

print("-" * 30)

df.columns = ["column1", "column2", "column3"]
print(df)
