import numpy as np
import pandas as pd
from tqdm import tqdm
import pickle as pickle
ratings_data = pd.read_csv("ratings.csv")
print(ratings_data.head())

movie_data = ratings_data.drop('timestamp', axis=1)

with open('users_by_film_dictionary.pkl', 'rb') as f:
    users_by_film_dictionary = pickle.load(f)

with open('movie_data_by_film.pkl', 'rb') as f:
    movie_data_by_film = pickle.load(f)

intersect_users_dict = {}
movies_ids = list(users_by_film_dictionary.keys())
for i in range(len(movies_ids)):
    movie_id_1 = movies_ids[i]
    users_1 = users_by_film_dictionary[movie_id_1]
    movie_1 = movie_data_by_film[movie_id_1]
    for j in tqdm(range(i + 1, len(movies_ids))):
        #         if (movie_id_1 == movie_id_2):
        #             continue
        #         if (movie_id_2,movie_id_1) in intersect_users_dict:
        #             continue
        movie_id_2 = movies_ids[j]
        movie_2 = movie_data_by_film[movie_id_2]
        users_2 = users_by_film_dictionary[movie_id_2]

        #         intersect_users = movie_2[movie_2['userId'].isin(users_1)]['userId']
        #         r_k_j = movie_1[(movie_1['userId'].isin(intersect_users))]['rating'].mean()
        #         r_k_i = movie_2[(movie_2['userId'].isin(intersect_users))]['rating'].mean()

        r_k_j = movie_1.loc[(movie_1['userId'].isin(users_2)), 'rating'].mean()
        r_k_i = movie_2.loc[(movie_2['userId'].isin(users_1)), 'rating'].mean()

        intersect_users_dict[(movie_id_1, movie_id_2)] = r_k_j - r_k_i
#         movie_2.loc[movie_2['userId'].isin(users_1),'userId']