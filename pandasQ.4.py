# write a panda program to select the 'name' and 'score' columns from the following dataframe

import pandas as np


data = {'name': ['anastasia','Dima','katherine','james','emily','michael','matthew', 'laura', 'kevin', 'jonas'],
        'score': [12.5,9,16.5,np.NaT,9,20,14.5,np.NaT,8,19],
        'attempts': [1,3,2,3,2,3,1,1,2,1]}

df = np.DataFrame(data)


selected_columns = df[['name', 'score']]


print(selected_columns)
