from ML import decision_tree, logistic_regression, random_forest, support_vector_machine
import matplotlib.pyplot as plt

logistic_regression_accuracy = logistic_regression.accuracy
logistic_regression_precision = logistic_regression.precision
logistic_regression_recall = logistic_regression.recall
logistic_regression_f1 = logistic_regression.f1

decision_tree_accuracy = decision_tree.accuracy
decision_tree_precision = decision_tree.precision
decision_tree_recall = decision_tree.recall
decision_tree_f1 = decision_tree.f1

random_forest_accuracy = random_forest.accuracy
random_forest_precision = random_forest.precision
random_forest_recall = random_forest.recall
random_forest_f1 = random_forest.f1

support_vector_machine_accuracy = support_vector_machine.accuracy
support_vector_machine_precision = support_vector_machine.precision
support_vector_machine_recall = support_vector_machine.recall
support_vector_machine_f1 = support_vector_machine.f1

x = [0, 0.25, 0.5, 0.75]

plt.figure(figsize=(12.5, 7.5))
plt.subplots_adjust(wspace=0.25, hspace=0.25)

plt.subplot(2, 2, 1)
plt.bar(x, [i * 100 for i in [logistic_regression_accuracy, decision_tree_accuracy, random_forest_accuracy,
                              support_vector_machine_accuracy]], width=0.125, color='red')
plt.xticks(x, ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM'], fontsize=9)
plt.ylim([0, 100])
plt.title('Accuracy')

plt.subplot(2, 2, 2)
plt.bar(x, [i * 100 for i in [logistic_regression_precision, decision_tree_precision, random_forest_precision,
                              support_vector_machine_precision]], width=0.125, color='yellow')
plt.xticks(x, ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM'], fontsize=9)
plt.ylim([0, 100])
plt.title('Precision')

plt.subplot(2, 2, 3)
plt.bar(x, [i * 100 for i in
            [logistic_regression_recall, decision_tree_recall, random_forest_recall, support_vector_machine_recall]],
        width=0.125, color='blue')
plt.xticks(x, ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM'], fontsize=9)
plt.ylim([0, 100])
plt.title('Recall')

plt.subplot(2, 2, 4)
plt.bar(x, [i * 100 for i in [logistic_regression_f1, decision_tree_f1, random_forest_f1, support_vector_machine_f1]],
        width=0.125, color='green')
plt.xticks(x, ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM'], fontsize=9)
plt.ylim([0, 100])
plt.title('F1 Score')

plt.show()
