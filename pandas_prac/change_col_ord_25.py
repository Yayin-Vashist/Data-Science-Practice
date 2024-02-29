import pandas as pd
import numpy as np

info = {"col1": [0, 1, 4, 7], "col2": [1, 2, 5, 8], "col3": [2, 3, 6, 9]}

df = pd.DataFrame(info)

df = df[["col3", "col2", "col1"]]

print(df)
