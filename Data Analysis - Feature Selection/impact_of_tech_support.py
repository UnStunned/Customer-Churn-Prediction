import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

tech_support = initial_dataset['TechSupport']
tech_support_count = tech_support.value_counts().sort_index()
tech_support_keys = list(dict(tech_support_count).keys())
tech_support_values = list(dict(tech_support_count).values())

x_labels = tech_support_keys
x = [0, 0.25, 0.5]
y = tech_support_values

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=8)

tech_support_churn = initial_dataset[['TechSupport','Churn']]
tech_support_churn_count = tech_support_churn.value_counts().sort_index()
tech_support_churn_keys = list(dict(tech_support_churn_count).keys())
tech_support_churn_values = list(dict(tech_support_churn_count).values())

No = []
Yes = []

for i in range(len(tech_support_churn_keys)):
    if tech_support_churn_keys[i][1] == 'No':
        No.append(tech_support_churn_values[i])
    else:
        Yes.append(tech_support_churn_values[i])

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