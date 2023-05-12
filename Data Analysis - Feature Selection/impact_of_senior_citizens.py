import pandas as pd
import matplotlib.pyplot as plt

initial_dataset = pd.read_csv('../customer.csv')
column_names = initial_dataset.columns

senior = initial_dataset['SeniorCitizen']
senior_count = senior.value_counts()
senior_churn = initial_dataset[['SeniorCitizen', 'Churn']]
senior_group = senior_churn.groupby('SeniorCitizen')
NoSenior = senior_group.get_group(0)
Senior = senior_group.get_group(1)
senior_count = dict(senior_count)
if senior_count.keys() == 0:
    senior_count["NoSenior"] = senior_count[0]
    del senior_count[0]
else:
    senior_count["Senior"] = senior_count.pop(1)
x_labels = ['Not a senior citizen', 'Senior citizen']
x = [0, 0.2]
y = list(senior_count.values())

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.ylim([0, 6000])
plt.xticks(x, labels=x_labels)
plt.bar(x, y, width=0.15)

Senior_churns = list(dict(Senior.value_counts()).values())
NoSenior_churns = list(dict(NoSenior.value_counts()).values())

y1 = [NoSenior_churns[0], Senior_churns[0]]
y2 = [NoSenior_churns[1], Senior_churns[1]]

x = [0, 0.35]
plt.subplot(1, 2, 2)
plt.bar(x, y1, width=0.15)
plt.bar([i + 0.15 for i in x], y2, width=0.15)
plt.xticks([i + 0.075 for i in x], labels=x_labels)
plt.show()

churn_ratio = [y2[i]/y1[i] for i in range(2)]
print(churn_ratio)

del column_names, senior, senior_count, senior_churn, senior_group, NoSenior, Senior, Senior_churns, NoSenior_churns, \
    x_labels, x, y, y1, y2
