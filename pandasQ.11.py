# write a pand a program to display the dimensions or shape of the world alcohol consuption data0set . also extract the column names from tha dataset 

import pandas as pd

# Load the world alcohol consumption dataset (replace with your dataset path)
# df = pd.read_csv('your_dataset.csv')

# Sample DataFrame (comment out the above line and uncomment the one above to load your dataset)
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany'],
    'Year': [2019, 2019, 2019, 2019],
    'Alcohol Consumption (L)': [8.5, 7.2, 10.4, 11.2]
}

df = pd.DataFrame(data)

# Display the shape (dimensions) of the DataFrame
shape = df.shape
print("Shape of the DataFrame:", shape)

# Extract and display the column names
column_names = df.columns.tolist()
print("Column Names:", column_names)
