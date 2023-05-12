import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

paperless_billing = initial_dataset['PaperlessBilling']
paperless_billing_count = paperless_billing.value_counts()
paperless_billing_dict = dict(paperless_billing.value_counts())
paperless_billing_keys = list(paperless_billing_dict.keys())
paperless_billing_values = list(paperless_billing_dict.values())

x_labels = ['Paperless Billing', 'No Paperless Billing']
x = [0, 0.25]
y = paperless_billing_values

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=8)

paperless_billing_churn = initial_dataset[['PaperlessBilling', 'Churn']]
paperless_billing_churn_group = paperless_billing_churn.groupby('PaperlessBilling')
paperless_billing_churn_dict = dict(paperless_billing_churn_group.value_counts())
paperless_billing_churn_dict_keys = list(paperless_billing_churn_dict.keys())
paperless_billing_churn_dict_values = list(paperless_billing_churn_dict.values())

No = []
Yes = []

for i in range(len(paperless_billing_churn_dict_keys)):
    if paperless_billing_churn_dict_keys[i][1] == 'No':
        No.append(paperless_billing_churn_dict_values[i])
    else:
        Yes.append(paperless_billing_churn_dict_values[i])

No[0], No[1] = No[1], No[0]
Yes[0], Yes[1] = Yes[1], Yes[0]

x = [0, 0.5]
y1 = No
y2 = Yes

plt.subplot(1, 2, 2)
plt.bar(x, y1, width=0.2)
plt.bar([i + 0.2 for i in x], y2, width=0.2)
plt.xticks([i + 0.1 for i in x], x_labels, fontsize=8)
plt.show()

churn_ratio = [Yes[i] / No[i] for i in range(len(Yes))]
print(churn_ratio)
