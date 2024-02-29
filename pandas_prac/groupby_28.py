import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
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
        "city": [
            "California",
            "Los Angeles",
            "California",
            "California",
            "California",
            "Los Angeles",
            "Los Angeles",
            "Georgia",
            "Georgia",
            "Los Angeles",
        ],
    }
)

grouped_df = df.groupby(["city"])

###########################################################To print the groups in grouped_df##################################################################

# This is 1st approach
# --> Here you can control the groups you want to get printed

# for key, item in grouped_df:
#    print(grouped_df.get_group(key), "\n\n")

# This is 2nd approach to do the same thing
# --> Here, You cannot control the groups you want to get printed

# for key, value in grouped_df:
#    print(value, end="\n\n\n")


##############################################################Print the count in the groups#################################################################

print(grouped_df.size(), end="\n\n\n")

print(grouped_df.size().reset_index(name="Number of people"))
