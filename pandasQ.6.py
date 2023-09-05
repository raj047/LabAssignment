# write a panda program to select the row where the score is mising i.g. is NaN 

import pandas as pd


data = {'name': ['anastasia','Dima','katherine','james','emily','michael','matthew', 'laura', 'kevin', 'jonas'],
        'score': [12.5,9,16.5,pd.NaT,9,20,14.5,pd.NaT,8,19],
        'attempts': [1,3,2,3,2,3,1,1,2,1]}

df = pd.DataFrame(data)


selected_rows = df[pd.isna(df['score'])]


print(selected_rows)
