import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

initial_dataset = pd.read_csv('../customer.csv')
tenure = initial_dataset['tenure'].sort_values()
keys = list(tenure.groupby(tenure).value_counts().keys())
keys = [i[1] for i in keys]
values = list(tenure.groupby(tenure).value_counts().values)
# print(keys)
# print(values)

y = []
bins = [10, 20, 30, 40, 50, 60, 70, 80]

s = 0

for i in bins:
    s = 0
    for j in keys:
        if j < i:
            s = s + values[keys.index(j)]
        else:
            y.append(s)
            break

y.append(s)

for _ in range(len(y) - 1, 0, -1):
    y[_] = y[_] - y[_ - 1]

x_labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']

plt.figure(figsize=(20, 6.25))

plt.subplot(1, 2, 1)
plt.xlabel('Tenure')
plt.ylabel('Number of customers')
plt.bar(x_labels, y)

tenure_churn = pd.concat([initial_dataset['tenure'], initial_dataset['Churn']], axis=1).sort_values('tenure')
tenure_churn_set = []

for i in range(len(bins)):
    if i == 0:
        r = tenure_churn.loc[(tenure_churn['tenure'] < bins[i])]
    else:
        r = tenure_churn.loc[(tenure_churn['tenure'] < bins[i]) & (tenure_churn['tenure'] > bins[i - 1])]
    r = r.drop(columns='tenure')
    No = list(dict(r.value_counts()).values())[0]
    Yes = list(dict(r.value_counts()).values())[1]
    tenure_churn_set.append((No, Yes))

No = [i[0] for i in tenure_churn_set]
Yes = [i[1] for i in tenure_churn_set]

x = np.arange(0, len(No))

plt.subplot(1, 2, 2)
plt.bar(x, No, width=0.2, label="Did not churn")
plt.bar([i + 0.2 for i in x], Yes, width=0.2, label="Did churn")
plt.xticks([i + 0.1 for i in x], x_labels)
plt.xlabel('Tenure')
plt.ylabel('Number of customers')
plt.legend()
plt.show()

churn_ratio = [Yes[i] / No[i] for i in range(len(Yes))]
print(churn_ratio)

del tenure, tenure_churn, tenure_churn_set, y, x, x_labels, bins, s, values, No, Yes, churn_ratio, initial_dataset
