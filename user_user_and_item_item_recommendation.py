import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.impute import SimpleImputer
import random

#Options required to print the whole dataframe in console
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

def na_values_fill_by_mean(matrix):

    #Fill na values user rating mean
    matrix=matrix.apply(lambda row: row.fillna(row.mean()), axis=1)
    
    return matrix

def na_values_fill_by_median(matrix):

    #Fill na values using matrix factorization
    matrix=matrix.fillna(np.nan)

    imputer=SimpleImputer(missing_values=np.nan, strategy='median')

    matrix=full_matrix()

    matrix=imputer.fit_transform(matrix)

    matrix=pd.DataFrame(matrix)

    return movie_user_matrix

def prediction_setup():

    #Read in the data file
    input = pd.read_csv("input_data/input_file.csv")

    #Get count of number of movies
    movies_count=len(input['movieId'].unique().tolist())

    #Get count of number of users
    user_count=len(input['userId'].unique().tolist())

    #Dummy data to fill the pandas user_movie_matrix dataframe
    empty_data=np.zeros((user_count, movies_count))

    #Fill user_movie_comparison matrix with user_id as row headers and movie id as column headers
    user_movie_matrix=pd.DataFrame(empty_data,columns=list(input['movieId'].unique()))
    user_movie_matrix.index=list(input['userId'].unique())

    #Make a movie user matrix with MovieId as Row Headers and column headers as UserId
    movie_user_matrix=input.pivot(index="movieId",columns="userId",values="rating")

    #Add a column for each movieId where the value is the average rating the movie got
    movie_user_matrix['mean'] = movie_user_matrix.mean(axis=1)

    movie_user_matrix=na_values_fill_by_mean(movie_user_matrix)

    #movie_user_matrix=na_values_fill_by_median(movie_user_matrix)

    return movie_user_matrix

def unique_movie_id_counts():

    # Read in the data file
    input = pd.read_csv("input_data/input_file.csv")

    # Get unique movie id's to be put in user-movie matrix
    movies_id_collection = input['movieId'].unique().tolist()

    return movies_id_collection

def unique_users_id_counts():

    # Read in the data file
    input = pd.read_csv("input_data/input_file.csv")

    # Get user id's to be put in user-movie matrix
    user_id_collection = input['userId'].unique().tolist()

    return user_id_collection

#Get user similarity
def user_similarity(input):

    #Get user similarity
    user_similarity = pairwise_distances(input, metric='cosine')

    return user_similarity

# Get item similarity
def item_similarity(input):

    # Get user similarity
    item_similarity = pairwise_distances(input.T, metric='cosine')

    return item_similarity

def overall_prediction(similarity, type):

    #Read in the movie-user matrix
    data_matrix = pd.read_csv("input_data/movie_user_matrix.csv")

    if type == 'user':

        #Get mean rating
        mean_user_rating=data_matrix.mean(axis=1)

        #Get rating difference
        ratings_diff = (data_matrix - mean_user_rating[:, np.newaxis])

        #Get prediction
        prediction = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T

    elif type == 'item':
        prediction = data_matrix.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])

    return prediction


def movies_prediction_by_items(movie_similarity_scores,movie_ids,input_movie):

    #Read in the data file
    input = pd.read_csv("input_data/input_file.csv")

    #Unique movie ids
    ids=movie_ids

    #Individual movie similarity scores
    scores=movie_similarity_scores

    #Merge individual id and similarity scores
    id_and_scores=dict(zip(ids, scores))

    #Sort id and scores as per scores
    id_and_scores_sorted = dict(sorted(id_and_scores.items(), key=lambda x: x[1], reverse=True))

    #Print Query movie name
    query_movie=input.loc[input['movieId'] == input_movie]
    query_movie=query_movie.sample(n=1)
    print("Query Movie:", query_movie['title'])

    #Iterator used to get only 15 movie recommendations
    iterator_for_recommendations = 0
    #Get movie recommendations
    for key in id_and_scores_sorted.keys():
        movie_row = input.loc[input['movieId'] == key]
        if iterator_for_recommendations<15:
            print(movie_row['title'].unique())
        iterator_for_recommendations+=1

def movies_prediction_by_users(user_similarity_scores,user_ids,movie_ids):

    #Read in the data file
    input = pd.read_csv("input_data/input_file.csv")

    #Unique user ids
    ids=user_ids

    #Individual user similarity scores
    user_scores=user_similarity_scores

    #Merge individual id and similarity scores
    id_and_scores=dict(zip(ids, user_scores))

    #Sort id and scores as per scores to get similar users in decreasing order
    sorted_new = dict(sorted(id_and_scores.items(), key=lambda x: x[1], reverse=True))

    #Take 5 most similar users
    most_similar_users=list(sorted_new.items())[:5]
    print(most_similar_users)
    most_similar_user_ids=[i[0] for i in most_similar_users]

    # #Get similar user-wise movie recommendations
    for i in most_similar_user_ids:
        similar_users_data_row = input.loc[input['userId'] == i]
        all_top_rated_movies_by_similar_users=similar_users_data_row[similar_users_data_row['rating']>3]['title']
        list_of_movies=list(all_top_rated_movies_by_similar_users)
        movies_to_be_recommended=random.sample(list_of_movies,5)
        print(movies_to_be_recommended)


