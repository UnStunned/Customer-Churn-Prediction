import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

multiple_lines = initial_dataset['MultipleLines']
multiple_lines_count = multiple_lines.value_counts().sort_index()
multiple_lines_keys = list(dict(multiple_lines_count).keys())
multiple_lines_values = list(dict(multiple_lines_count).values())
print(multiple_lines_keys, multiple_lines_values)

x_labels = multiple_lines_keys
x = [0, 0.25, 0.5]
y = multiple_lines_values

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=8)

multiple_lines_churn = initial_dataset[['MultipleLines', 'Churn']]
multiple_lines_churn_count = multiple_lines_churn.value_counts().sort_index()
multiple_lines_churn_keys = list(dict(multiple_lines_churn_count).keys())
multiple_lines_churn_values = list(dict(multiple_lines_churn_count).values())
print(multiple_lines_churn_keys, multiple_lines_churn_values)

No = []
Yes = []

for i in range(len(multiple_lines_churn_keys)):
    if multiple_lines_churn_keys[i][1] == 'No':
        No.append(multiple_lines_churn_values[i])
    else:
        Yes.append(multiple_lines_churn_values[i])

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
