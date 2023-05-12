import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

streaming_tv = initial_dataset['StreamingTV']
streaming_tv_count = streaming_tv.value_counts().sort_index()
streaming_tv_keys = list(dict(streaming_tv_count).keys())
streaming_tv_values = list(dict(streaming_tv_count).values())

x_labels = streaming_tv_keys
x = [0, 0.25, 0.5]
y = streaming_tv_values

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=8)

streaming_tv_churn = initial_dataset[['StreamingTV', 'Churn']]
streaming_tv_churn_count = streaming_tv_churn.value_counts().sort_index()
streaming_tv_churn_keys = list(dict(streaming_tv_churn_count).keys())
streaming_tv_churn_values = list(dict(streaming_tv_churn_count).values())

No = []
Yes = []

for i in range(len(streaming_tv_churn_keys)):
    if streaming_tv_churn_keys[i][1] == 'No':
        No.append(streaming_tv_churn_values[i])
    else:
        Yes.append(streaming_tv_churn_values[i])

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
