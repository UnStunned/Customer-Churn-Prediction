import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

payment_method = initial_dataset['PaymentMethod']
payment_method_count = payment_method.value_counts()
payment_method_count_dict = dict(payment_method_count)
payment_method_keys = list(payment_method_count_dict.keys())
payment_method_values = list(payment_method_count_dict.values())

payment_method_keys[2] = 'Bank Transfer'
payment_method_keys[3] = 'Credit Card'

plt.figure(figsize=(15, 7.5))

x_labels = payment_method_keys
y = payment_method_values
x = [0, 0.5, 1, 1.5]

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=10)

payment_method_churn = initial_dataset[['PaymentMethod', 'Churn']]
payment_method_group = payment_method_churn.groupby('PaymentMethod')
payment_method_group_count = payment_method_group.value_counts()
payment_method_group_dict = dict(payment_method_group_count)

payment_method_group_keys = list(payment_method_group_dict.keys())
payment_method_group_values = list(payment_method_group_dict.values())

No = []
Yes = []

for i in range(len(payment_method_group_keys)):
    if payment_method_group_keys[i][1] == 'No':
        No.append(payment_method_group_values[i])
    else:
        Yes.append(payment_method_group_values[i])

No[0], No[2] = No[2], No[0]
No[1], No[3] = No[3], No[1]

Yes[0], Yes[2] = Yes[2], Yes[0]
Yes[1], Yes[3] = Yes[3], Yes[1]

x_labels = payment_method_keys
y1 = No
y2 = Yes
x = [0, 0.5, 1, 1.5]

plt.subplot(1, 2, 2)
plt.bar(x, y1, width=0.2)
plt.bar([i + 0.2 for i in x], y2, width=0.2)
plt.xticks([i + 0.1 for i in x], x_labels, fontsize=10)
plt.show()

churn_ratio = [Yes[i] / No[i] for i in range(len(Yes))]
print(churn_ratio)
