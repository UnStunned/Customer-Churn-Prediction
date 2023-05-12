import pandas as pd

data = pd.read_csv('final_data.csv')

attribute = []
count = []

# Getting the number of enteries which is the user count
attribute.append('Users')
count.append(len(data))

# Getting the total spendings of all customers
attribute.append('Value')
count.append(int(round(sum(list(data['TotalCharges'])), 0)))

# Getting total number of churners
attribute.append('Churners')
count.append(data['Churn'].value_counts()['Yes'])

# Getting churn based on months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i in range(len((data['MonthOfChurn'].value_counts())) - 1):
    month_name = months[i]
    attribute.append(month_name)
    count.append(data['MonthOfChurn'].value_counts()[month_name])

backend_data = pd.DataFrame()
backend_data['Attribute'] = attribute
backend_data['Count'] = count

backend_data.to_csv('backend_data.csv', index=False)


