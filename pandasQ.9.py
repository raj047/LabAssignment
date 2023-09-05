# write a panda program to join two given  dataframe along colomns  and asign all data

import pandas as pd

# Sample DataFrames
data1 = {'name': ['Alice', 'Bob'],
         'score': [85, 92]}

data2 = {'age': [25, 30],
         'city': ['New York', 'Los Angeles']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Join the DataFrames along columns and assign all data
combined_df = pd.concat([df1, df2], axis=1)

# Display the combined DataFrame
print(combined_df)
