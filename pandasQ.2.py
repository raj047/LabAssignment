import pandas as pd

# Create a dictionary with data and specified index labels
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

index_labels = ['Person 1', 'Person 2', 'Person 3', 'Person 4']

# Create a DataFrame from the dictionary with specified index
df = pd.DataFrame(data, index=index_labels)

# Display the DataFrame
print(df)
