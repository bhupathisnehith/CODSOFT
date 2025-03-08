import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


data = {
    'User': ['User1', 'User1', 'User1', 'User2', 'User2', 'User2', 'User3', 'User3', 'User3', 'User4', 'User4', 'User4',
             'User5', 'User5', 'User5', 'User6', 'User6', 'User6', 'User7', 'User7', 'User7'],
    'Item': ['Movie1', 'Movie2', 'Movie3', 'Movie1', 'Movie2', 'Movie4', 'Movie2', 'Movie3', 'Movie5', 'Movie1', 'Movie3', 'Movie4',
             'Movie3', 'Movie4', 'Movie5', 'Movie1', 'Movie2', 'Movie5', 'Movie2', 'Movie3', 'Movie4'],
    'Rating': [5, 4, 3, 4, 5, 2, 4, 5, 5, 3, 2, 5, 5, 4, 3, 4, 3, 5, 2, 4, 5]
}


df = pd.DataFrame(data)


user_item_matrix = df.pivot_table(index='User', columns='Item', values='Rating').fillna(0)

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def recommend_items(user, user_similarity_df, user_item_matrix, n_recommendations=2):

    similar_users = user_similarity_df[user].sort_values(ascending=False)[1:]  # Exclude the user itself

    unrated_items = user_item_matrix.loc[user][user_item_matrix.loc[user] == 0].index

    recommendations = {}
    for item in unrated_items:
        weighted_sum = 0
        similarity_sum = 0
        for other_user in similar_users.index:
            if user_item_matrix.loc[other_user, item] != 0:
                weighted_sum += user_similarity_df.loc[user, other_user] * user_item_matrix.loc[other_user, item]
                similarity_sum += user_similarity_df.loc[user, other_user]
        if similarity_sum != 0:
            recommendations[item] = weighted_sum / similarity_sum

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

    return sorted_recommendations[:n_recommendations]

user_name = input("Enter your user name (e.g., User1, User2, etc.): ")

if user_name in user_item_matrix.index:
    recommendations = recommend_items(user_name, user_similarity_df, user_item_matrix)
    print(f"Recommendations for {user_name}: {recommendations}")
else:
    print("User not found. Please try again.")

items = {
    'Item': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Genre': ['Action, Adventure', 'Comedy, Romance', 'Action, Thriller', 'Comedy, Drama', 'Action, Drama']
}

items_df = pd.DataFrame(items)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(items_df['Genre'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend_similar_items(item, cosine_sim, items_df, n_recommendations=2):
    
    idx = items_df.index[items_df['Item'] == item].tolist()[0]

    
    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:n_recommendations+1]

    item_indices = [i[0] for i in sim_scores]

    return items_df['Item'].iloc[item_indices]

item_name = input("Enter an item name (e.g., Movie1, Movie2, etc.): ")

if item_name in items_df['Item'].values:
    recommendations = recommend_similar_items(item_name, cosine_sim, items_df)
    print(f"Recommendations for {item_name}: {list(recommendations)}")
else:
    print("Item not found. Please try again.")


***OUTPUT:****
EXAMPLE 1:
Enter your user name (e.g., User1, User2, etc.): User3
Recommendations for User3: [('Movie1', 4.194218806599868), ('Movie4', 3.988455413596195)]
Enter an item name (e.g., Movie1, Movie2, etc.): Movie1
Recommendations for Movie1: ['Movie5', 'Movie3']

EXAMPLE 2:
Enter your user name (e.g., User1, User2, etc.): User1
Recommendations for User1: [('Movie4', 4.0), ('Movie5', 4.0)]
**Additional Details:**
If the user enters a name or item that is not found in the dataset, the program will display:
User not found. Please try again.
(OR)
Item not found. Please try again.



