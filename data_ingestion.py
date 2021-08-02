import pandas as pd
from zipfile import ZipFile

def merging_files():

    with ZipFile('input_data.zip', 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall('input_data')
        print('File is unzipped in temp folder')

    #Contains Movie Id, Title and Genre/s
    movies= pd.read_table("input_data/movies.dat", sep="::")
    movies.columns=['movieId','title','genre']

    #Contains User Id, Movie Id, Rating and Timestamp
    ratings= pd.read_table("input_data/ratings.dat", sep="::")
    ratings.columns=['userId','movieId','rating','timestamp']

    #Merging movies dataframe and ratings dataframe on basis of movieId
    movies_and_ratings=pd.merge(movies, ratings, on='movieId')

    movies_and_ratings.to_csv('input_data/input_file.csv', index=False)

merging_files()

