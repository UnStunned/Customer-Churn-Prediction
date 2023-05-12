import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn import tree
import seaborn as sns


initial_dataset = pd.read_csv('../customer.csv')
selected_dataset = initial_dataset.drop(columns=['customerID', 'gender', 'PhoneService'])
remainder_dataset = initial_dataset[['tenure', 'MonthlyCharges', 'TotalCharges']]

# creation of dummy variables to handle categorical data
intermediate_dataset_1 = pd.DataFrame(selected_dataset)
intermediate_dataset_1 = intermediate_dataset_1.drop(
    ['SeniorCitizen', 'Partner', 'Dependents', 'Churn', 'PaperlessBilling', 'tenure', 'MonthlyCharges',
     'TotalCharges'], axis=1)
intermediate_dataset_1 = (pd.get_dummies(intermediate_dataset_1))
intermediate_dataset_1 = intermediate_dataset_1.drop(
    columns=['MultipleLines_No phone service', 'InternetService_No', 'OnlineSecurity_No internet service',
             'OnlineBackup_No internet service', 'DeviceProtection_No internet service',
             'TechSupport_No internet service', 'StreamingTV_No internet service',
             'StreamingMovies_No internet service', 'Contract_One year', 'PaymentMethod_Credit card (automatic)'])

# Binary Categories
intermediate_dataset_2 = selected_dataset[
    ['SeniorCitizen', 'Partner', 'Dependents', 'PaperlessBilling', 'Churn']].replace('Yes',
                                                                                     1)
intermediate_dataset_2 = intermediate_dataset_2[
    ['SeniorCitizen', 'Partner', 'Dependents', 'PaperlessBilling', 'Churn']].replace('No', 0)

selected_dataset = pd.concat([remainder_dataset, intermediate_dataset_1, intermediate_dataset_2], axis=1)
selected_dataset = selected_dataset.dropna(axis=0)

X_columns = list(selected_dataset.columns)
X_columns[0], X_columns[6] = X_columns[6], X_columns[0]
X_columns.remove('Churn')
y_column = 'Churn'

X_train, X_test, y_train, y_test = train_test_split(selected_dataset[X_columns], selected_dataset[y_column],
                                                    test_size=0.25, random_state=52)
decision_tree = tree.DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)
prediction = decision_tree.predict(X_test)
accuracy = decision_tree.score(X_test, y_test)
f1 = f1_score(y_test, prediction)
prediction = decision_tree.predict(X_test)
conf_matrix = confusion_matrix(y_test, prediction)

if __name__ == '__main__':
    plt.figure(figsize=(10, 7.5))
    sns.heatmap(conf_matrix, cmap='Blues', annot=True, fmt="d")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

precision = precision_score(y_test, prediction)
recall = recall_score(y_test, prediction)

if __name__ == '__main__':
    print(f'Accuracy of decision tree on customer churn is {accuracy*100}')
    # print(f'Precision of decision tree on customer churn is {precision}')
    # print(f'Recall of decision tree on customer churn is {recall}')
    # print(f'F1 score of decision tree on customer churn is {f1}')
