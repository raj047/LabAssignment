# write a panda program to join two given  dataframe along rows  and asign all data

import pandas as pd

data1 = {'name': ['Alice', 'Bob'],
         'score': [85, 92]}

data2 = {'name': ['Charlie', 'David'],
         'score': [78, 95]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


combined_df = pd.concat([df1, df2], ignore_index=True)


print(combined_df)
