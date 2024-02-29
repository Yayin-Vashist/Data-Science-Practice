import numpy as np
import pandas as pd
from pandas.core.common import index_labels_to_array

exam_data = {
    "name": [
        "Anastasia",
        "Dima",
        "Katherine",
        "James",
        "Emily",
        "Michael",
        "Matthew",
        "Laura",
        "Kevin",
        "Jonas",
    ],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(exam_data, index=labels)

new_row = {"name": "Suresh", "score": 15.5, "attempts": 1, "qualify": "yes"}


print("-" * 30 + "Original DataFrame" + "-" * 30)
print(df)

new_df = pd.DataFrame(new_row, index=["k"])
df = df._append(new_df)

print("-" * 30 + "New DataFrame" + "-" * 30)

print(df)


df = df.drop("k", axis=0)
print("-" * 30 + "Back To Original" + "-" * 30)


print(df)
