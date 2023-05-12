import matplotlib.pyplot as plt
import pandas as pd

initial_dataset = pd.read_csv('../customer.csv')

contract = initial_dataset['Contract']
contract_count = contract.value_counts().sort_index()
contract_count_dict = dict(contract_count)
contract_keys = list(contract_count_dict.keys())
contract_values = list(contract_count_dict.values())

x_labels = contract_keys
x = [0, 0.25, 0.5]
y = contract_values

plt.subplot(1, 2, 1)
plt.bar(x, y, width=0.2)
plt.xticks(x, x_labels, fontsize=8)

contract_churn = initial_dataset[['Contract', 'Churn']]
contract_churn_counts = contract_churn.value_counts().sort_index()
contract_churn_dict = dict(contract_churn_counts)
contract_churn_keys = list(contract_churn_dict.keys())
contract_churn_values = list(contract_churn_dict.values())

No = []
Yes = []

for i in range(len(contract_churn_keys)):
    if contract_churn_keys[i][1] == 'No':
        No.append(contract_churn_values[i])
    else:
        Yes.append(contract_churn_values[i])

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
