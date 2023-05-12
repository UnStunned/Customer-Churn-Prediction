import pandas as pd

def get_number_of_words(phrase):
    words = 0
    for _ in phrase:
        if _ == " ":
            words += 1
    return words


customer_file = pd.read_csv('./customer.csv')
churn = customer_file
churn = churn.groupby('Churn')
No_churn = churn.get_group('No')
Yes_churn = churn.get_group('Yes')

# print(len(Yes_churn))
# print(len(No_churn))
# print(customer_file)

review_file = pd.read_csv('./reviews.csv')
electronics_reviews = review_file[['category','rating', 'text_']]
electronics_reviews = electronics_reviews[electronics_reviews['category'] == 'Electronics_5']
# print(electronics_reviews)

tools_review = review_file[['category','rating', 'text_']]
tools_review = tools_review[tools_review['category'] == 'Tools_and_Home_Improvement_5']
# print(tools_review)

reviews = pd.concat([electronics_reviews, tools_review])
reviews = reviews.drop('category', axis=1)
reviews = reviews.groupby('rating')
rating_1 = reviews.get_group(1.0)
rating_2 = reviews.get_group(2.0)
rating_3 = reviews.get_group(3.0)
rating_4 = reviews.get_group(4.0)
rating_5 = reviews.get_group(5.0)

negative = pd.concat([rating_1, rating_2, rating_3])
positive = pd.concat([rating_4, rating_5])

negative = pd.concat([negative, positive.head(307)])
positive = positive.tail(n=5174)


# RESETTING THE INDEXING FOR JOIN
No_churn.reset_index(inplace = True)
Yes_churn.reset_index(inplace = True)
negative.reset_index(inplace = True)
positive.reset_index(inplace = True)

temp_1 = pd.concat([No_churn, positive], axis=1)
temp_2 = pd.concat([Yes_churn, negative], axis=1)

temp_1 = temp_1.drop(columns='index')
temp_2 = temp_2.drop(columns='index')

column_names = (list(No_churn.columns) + list(positive.columns))

final_data = pd.concat([temp_1, temp_2], axis=0)
final_data = final_data.sample(frac=1)
final_data['TotalCharges'] = final_data['TotalCharges'].fillna(0)

final_data.to_csv('final_data.csv', index=False)
