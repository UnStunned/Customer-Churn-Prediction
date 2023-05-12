import pandas as pd
import random

initial_dataset = pd.read_csv('./final_data.csv')
churn = list(initial_dataset['Churn'])

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

month_of_leaving = []

for i in range(len(churn)):
    if churn[i] == 'Yes':
        month_of_leaving.append(random.choices(months, [1, 4, 1, 8, 2, 12, 10, 8, 4, 3, 2, 1], k=1)[0])
    else:
        month_of_leaving.append('Not churned')

initial_dataset['MonthOfChurn'] = month_of_leaving

initial_dataset.to_csv('final_data.csv', index=False)