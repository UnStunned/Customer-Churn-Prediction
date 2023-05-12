import pandas as pd
import matplotlib.pyplot as plt

initial_dataset = pd.read_csv('../customer.csv')
column_names = initial_dataset.columns

genders = initial_dataset['gender']
gender_count = genders.value_counts()

gender_churn = initial_dataset[['gender', 'Churn']]
gender_group = gender_churn.groupby('gender')
females = gender_group.get_group('Female')
males = gender_group.get_group('Male')

gender_count = dict(gender_count)
x_labels = list(gender_count.keys())
x = [0, 0.2]
y = list(gender_count.values())

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.ylim([0, 4000])
plt.xticks(x, labels=x_labels)
plt.bar(x, y, width=0.15)

male_churns = list(dict(males.value_counts()).values())
female_churns = list(dict(females.value_counts()).values())

y1 = [male_churns[0], female_churns[0]]
y2 = [male_churns[1], female_churns[1]]

x = [0, 0.35]
plt.subplot(1, 2, 2)
plt.bar(x, y1, width=0.15)
plt.bar([i + 0.15 for i in x], y2, width=0.15)
plt.xticks([i+0.075 for i in x], labels=x_labels)
plt.show()


del column_names, genders, gender_count, gender_churn, gender_group, females, males, male_churns, female_churns, \
    x_labels, x, y, y1, y2
