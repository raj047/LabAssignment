# write a program to append rows to an existing dataframe and display the comnined data

import pandas as pd

# Existing DataFrame
data = {'name': ['Alice', 'Bob'],
        'score': [85, 92]}

df = pd.DataFrame(data)

# New data to append
new_data = {'name': ['Charlie', 'David'],
            'score': [78, 95]}

# Using pd.concat()
combined_df_concat = pd.concat([df, pd.DataFrame(new_data)])

# Using .append() method
df_to_append = pd.DataFrame(new_data)
combined_df_append = df.append(df_to_append)

# Display the combined DataFrames
print("Using pd.concat():")
print(combined_df_concat)

print("\nUsing .append() method:")
print(combined_df_append)
