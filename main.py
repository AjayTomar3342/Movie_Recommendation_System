import pandas
import pandas as pd

from data_ingestion import merging_files
from user_user_and_item_item_recommendation import prediction_setup
from user_user_and_item_item_recommendation import user_similarity
from user_user_and_item_item_recommendation import item_similarity
from user_user_and_item_item_recommendation import overall_prediction
from user_user_and_item_item_recommendation import movies_prediction_by_items
from user_user_and_item_item_recommendation import unique_movie_id_counts
from user_user_and_item_item_recommendation import unique_users_id_counts
from user_user_and_item_item_recommendation import movies_prediction_by_users

import numpy as np

#Part 1: Inputting Files(General Part)
#Data Ingestion
merging_files()

#Part 2.a.): Recommendation without any recommendation library
#Functions for recommendation using similarity without any recommendation library

#Get unique movie id numbers
unique_movie_ids=unique_movie_id_counts()

#Get unique user id numbers
unique_user_ids=unique_users_id_counts()

#Get user similarity prediction. This provides similar users. Recommendations can be made on basis of what most similar users like most
single_user=pd.DataFrame(overall_prediction(user_similarity(prediction_setup()),'user')).iloc[25]

#Get item similarity prediction
#single_movie = overall_prediction(item_similarity(prediction_setup()),'item').iloc[200]

#Predict similar movies as per items to the selected movie above
#movies_prediction_by_items(single_movie,unique_movie_ids,200)

#Predict similar movies as per users to the selected movie above
movies_prediction_by_users(single_user,unique_user_ids,unique_movie_ids)