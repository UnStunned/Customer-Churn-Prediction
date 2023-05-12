import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')
total_charges = initial_dataset['TotalCharges']
total_charges_mean = total_charges.mean()

two_groups = total_charges.groupby(total_charges <= total_charges_mean)
less_than_mean = two_groups.get_group(1)
greater_than_mean = two_groups.get_group(0)

x_labels = ['Low spenders', 'High spenders']
y = [len(less_than_mean), len(greater_than_mean)]
x = [0, 0.25]

print(y)

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels)

total_charges_churn = initial_dataset[['TotalCharges', 'Churn']]
total_charges_churn_mean = total_charges.mean()

two_groups = total_charges_churn.groupby(total_charges <= total_charges_churn_mean)
less_than_mean = two_groups.get_group(1)
greater_than_mean = two_groups.get_group(0)

No = []
Yes = []

reqd_dict = dict(less_than_mean.groupby('Churn').value_counts())
reqd_dict_keys = list(reqd_dict.keys())
reqd_dict_values = list(reqd_dict.values())

no_count = 0
yes_count = 0
for i in range(len(reqd_dict_keys)):
    if reqd_dict_keys[i][0] == 'No':
        no_count += reqd_dict_values[i]
    else:
        yes_count += reqd_dict_values[i]

No.append(no_count)
Yes.append(yes_count)

reqd_dict = dict(greater_than_mean.groupby('Churn').value_counts())
reqd_dict_keys = list(reqd_dict.keys())
reqd_dict_values = list(reqd_dict.values())

no_count = 0
yes_count = 0
for i in range(len(reqd_dict_keys)):
    if reqd_dict_keys[i][0] == 'No':
        no_count += reqd_dict_values[i]
    else:
        yes_count += reqd_dict_values[i]

No.append(no_count)
Yes.append(yes_count)

# No[0], No[1] = No[1], No[0]
# Yes[0], Yes[1] = Yes[1], Yes[0]

print(No, Yes)

y1 = No
y2 = Yes
x = [0, 0.5]

plt.subplot(1, 2, 2)
plt.bar(x, y1, width=0.2)
plt.bar([i + 0.2 for i in x], y2, width=0.2)
plt.xticks([i + 0.1 for i in x], x_labels)
plt.show()

churn_ratio = [Yes[i] / No[i] for i in range(len(Yes))]
print(churn_ratio)
