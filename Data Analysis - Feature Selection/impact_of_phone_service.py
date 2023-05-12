import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

initial_dataset = pd.read_csv('../customer.csv')

phone_service = initial_dataset['PhoneService']
phone_service_report = dict(phone_service.value_counts())
Yes = phone_service_report['Yes']
No = phone_service_report['No']

x = [0, 0.5]
y = [Yes, No]
x_labels = ['Have Phone Service', 'Do not have Phone Service']

plt.figure(figsize=(15,7.5))
plt.subplot(1,2,1)
plt.bar(x, y, width=0.2)
plt.xticks(x, labels=x_labels)

phone_service_churn = initial_dataset[['PhoneService', 'Churn']]
groups = phone_service_churn.groupby('PhoneService')
print(dict(groups.value_counts()))

# No Phone Service - Did not churn = 512
# No Phone Service - Did churn = 170
# Yes Phone Service - Did not churn = 4462
# Yes Phone Service - Did churn = 1699

y1 = [4662, 512]
y2 = [1699, 170]

plt.subplot(1,2,2)
plt.bar(x, y1, width=0.2, label='Did not churn')
plt.bar([i + 0.2 for i in x], y2, width=0.2, label='Did churn')
plt.xticks([i+0.1 for i in x], labels=x_labels)
plt.legend()
plt.show()

churn_ratio = [y2[i] / y1[i] for i in range(len(y1))]
print(churn_ratio)