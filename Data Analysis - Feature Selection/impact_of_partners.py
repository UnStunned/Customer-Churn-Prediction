import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np

initial_dataset = pd.read_csv('../customer.csv')
partner = initial_dataset['Partner']
partner = partner.replace('Yes', 'Has partner')
partner = partner.replace('No', 'Does not have partner')

partner_dict = dict(partner.value_counts())
# print(partner_dict)

have_partner = partner_dict['Has partner']
does_not_have_partner = partner_dict['Does not have partner']
# print(have_partner, does_not_have_partner)

# y = [have_partner, does_not_have_partner]
# x = [0, 0.5]
# plt.bar(x, y, width=0.25)
# plt.xticks(x, ['Has Partner', 'Does not have Partner'])
# plt.show()

churns = initial_dataset['Churn']
# print(churns)

partner_churns = pd.concat([partner, churns], axis=1)
partner_churn_groups = partner_churns.groupby('Partner')

# print(partner_churn_groups.value_counts())
partner_churn_dict = dict(partner_churn_groups.value_counts())
partner_churn_keys = list(partner_churn_dict.keys())
partner_churn_values = list(partner_churn_dict.values())
# print(partner_churn_keys, partner_churn_values)

No = []
Yes = []

for i in range(len(partner_churn_values)):
    if partner_churn_keys[i][1] == 'No':
        No.append(partner_churn_values[i])
    else:
        Yes.append(partner_churn_values[i])

No[0], No[1] = No[1], No[0]
Yes[0], Yes[1] = Yes[1], Yes[0]

plt.figure(figsize=(10, 7.5))
x_labels = ['Has Partner', 'Does not have partner']
x = [0, 0.5]
y1 = No
y2 = Yes
plt.bar(x, y1, width=0.2, label='Did not churn')
plt.bar([i + 0.2 for i in x], y2, width=0.2, label='Did churn')
plt.xticks([i + 0.1 for i in x], x_labels)
plt.legend()
plt.show()

churn_ratio = [Yes[i] / No[i] for i in range(len(Yes))]
print(churn_ratio)
