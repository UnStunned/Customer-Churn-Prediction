import pandas as pd
import matplotlib.pyplot as plt

initial_dataset = pd.read_csv('../customer.csv')
column_names = initial_dataset.columns

dependents = initial_dataset['Dependents']
dependents_count = dependents.value_counts()

dependents_churn = initial_dataset[['Dependents', 'Churn']]
dependents_group = dependents_churn.groupby('Dependents')
NoDependents = dependents_group.get_group('No')
Dependents= dependents_group.get_group('Yes')

dependents_count = dict(dependents_count)
x_labels = ['Does not have dependents', 'Has dependents']
x = [0, 0.2]
y = list(dependents_count.values())

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.ylim([0, 6000])
plt.xticks(x, labels=x_labels)
plt.bar(x, y, width=0.15)

dependents_churns = list(dict(Dependents.value_counts()).values())
NoDependents_churns = list(dict(NoDependents.value_counts()).values())

y1 = [NoDependents_churns[0], dependents_churns[0]]
y2 = [dependents_churns[1], dependents_churns[1]]

x = [0, 0.35]
plt.subplot(1, 2, 2)
plt.bar(x, y1, width=0.15)
plt.bar([i + 0.15 for i in x], y2, width=0.15)
plt.xticks([i+0.075 for i in x], labels=x_labels)
plt.show()

churn_ratio = [y2[i] / y1[i] for i in range(2)]
print(churn_ratio)

del column_names, dependents, dependents_count, dependents_churn, dependents_group, NoDependents, Dependents, dependents_churns, NoDependents_churns, \
    x_labels, x, y, y1, y2
