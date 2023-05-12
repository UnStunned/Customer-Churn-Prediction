import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

online_security = initial_dataset['OnlineSecurity']
online_security_count = online_security.value_counts().sort_index()
online_security_keys = list(dict(online_security_count).keys())
online_security_values = list(dict(online_security_count).values())

x_labels = online_security_keys
x = [0, 0.25, 0.5]
y = online_security_values

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=8)

online_security_churn = initial_dataset[['OnlineSecurity','Churn']]
online_security_churn_count = online_security_churn.value_counts().sort_index()
online_security_churn_keys = list(dict(online_security_churn_count).keys())
online_security_churn_values = list(dict(online_security_churn_count).values())

No = []
Yes = []

for i in range(len(online_security_churn_keys)):
    if online_security_churn_keys[i][1] == 'No':
        No.append(online_security_churn_values[i])
    else:
        Yes.append(online_security_churn_values[i])

x = [0, 0.5, 1]
y1 = No
y2 = Yes

plt.subplot(1, 2, 2)
plt.bar(x, y1, width=0.2)
plt.bar([i + 0.2 for i in x], y2, width=0.2)
plt.xticks([i + 0.1 for i in x], x_labels, fontsize=8)
plt.show()

churn_ratio = [Yes[i] / No[i] for i in range(len(Yes))]
print(churn_ratio)
