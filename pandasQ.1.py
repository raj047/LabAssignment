# write a pandas program to create a dataframe from a dictionary and display it
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}


df = pd.DataFrame(data)


print(df)
