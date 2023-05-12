import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

online_backup = initial_dataset['OnlineBackup']
online_backup_count = online_backup.value_counts().sort_index()
online_backup_keys = list(dict(online_backup_count).keys())
online_backup_values = list(dict(online_backup_count).values())

x_labels = online_backup_keys
x = [0, 0.25, 0.5]
y = online_backup_values

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=8)

online_backup_churn = initial_dataset[['OnlineBackup','Churn']]
online_backup_churn_count = online_backup_churn.value_counts().sort_index()
online_backup_churn_keys = list(dict(online_backup_churn_count).keys())
online_backup_churn_values = list(dict(online_backup_churn_count).values())

No = []
Yes = []

for i in range(len(online_backup_churn_keys)):
    if online_backup_churn_keys[i][1] == 'No':
        No.append(online_backup_churn_values[i])
    else:
        Yes.append(online_backup_churn_values[i])

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