# write a panda program to get the first 3 rows of given dataframe 

import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
}

df = pd.DataFrame(data)


first_3_rows = df.head(3)


print(first_3_rows)
