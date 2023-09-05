# write a panda program to select the row where the number of attempts in the examination is greater than 2

import pandas as pd


data = {'name': ['anastasia','Dima','katherine','james','emily','michael','matthew', 'laura', 'kevin', 'jonas'],
        'score': [12.5,9,16.5,6,9,20,14.5,7,8,19],
        'attempts': [1,3,2,3,2,3,1,1,2,1]}

df = pd.DataFrame(data)


selected_rows = df[df['attempts'] > 2]


print(selected_rows)
