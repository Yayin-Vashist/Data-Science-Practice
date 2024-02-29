import pandas as pd
import numpy as np

exam_data = [
    {"name": "Anastasia", "score": 12.5},
    {"name": "Dima", "score": 9},
    {"name": "Katherine", "score": 16.5},
]

df = pd.DataFrame(exam_data)

for index, rows in df.iterrows():
    for i in df:
        print(rows[i], end=" ")
    print("")
