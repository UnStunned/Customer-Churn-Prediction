import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

initial_dataset = pd.read_csv('../customer.csv')

internet_service = initial_dataset['InternetService']
internet_service_counts = dict(internet_service.value_counts())
internet_service_keys = list(internet_service.value_counts().keys())
internet_service_keys[2] = "No Internet"
internet_service_values = list(internet_service_counts.values())
print(internet_service_keys, internet_service_values)

x_labels = internet_service_keys
x = [0, 0.5, 1]
y = internet_service_values

# plt.bar(x, y, width=0.2)
# plt.xticks(x, x_labels)
# plt.show()

internet_service_churn = initial_dataset[['InternetService','Churn']]
internet_service_groups = dict(internet_service_churn.groupby('InternetService').value_counts())
internet_service_groups_keys = list(internet_service_groups.keys())
internet_service_groups_values = list(internet_service_groups.values())
print(internet_service_groups_keys, internet_service_groups_values)

no_churn = []
yes_churn = []

for i in range(len(internet_service_groups_keys)):
    if internet_service_groups_keys[i][1] == 'No':
        no_churn.append(internet_service_groups_values[i])
    else:
        yes_churn.append(internet_service_groups_values[i])

print(no_churn, yes_churn)

x_labels = ['DSL', 'Fibre optic', 'No internet']
y1 = no_churn
y2 = yes_churn

plt.bar(x, y1, width=0.2)
plt.bar([i+0.2 for i in x], y2, width=0.2)
plt.xticks([i+0.1 for i in x], x_labels)
plt.show()

churn_ratio = [yes_churn[i]/no_churn[i] for i in range(3)]
print(churn_ratio)