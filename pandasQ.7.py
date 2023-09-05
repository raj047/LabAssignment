# write the panda program to calculate the mean of all students' scores .data frame is stored in a dataframe

import pandas as pd


data = data = {'name': ['anastasia','Dima','katherine','james','emily','michael','matthew', 'laura', 'kevin', 'jonas'],
        'score': [12.5,9,16.5,pd.NaT,9,20,14.5,pd.NaT,8,19],
        'attempts': [1,3,2,3,2,3,1,1,2,1]}

df = pd.DataFrame(data)

mean_score = df['score'].mean()


print("Mean Score:", mean_score)
