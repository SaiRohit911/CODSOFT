import pandas as pd
from matplotlib import pyplot as plt

moviemeta = pd.read_csv('movies_metadata.csv')

moviemeta.head()

moviemeta.info()

meanvote = moviemeta['vote_average'].mean()
print(meanvote)

minimumvote = moviemeta['vote_count'].quantile(0.90)
print(minimumvote)

q_movies = moviemeta.copy().loc[moviemeta['vote_count'] >=minimumvote]
q_movies.shape

def weighted_rating(X, minimumvote=minimumvote, meanvote=meanvote):
    voters = X['vote_count']
    avg_vote = X['vote_average']
    return (voters/(voters+minimumvote) * avg_vote) + (minimumvote/(minimumvote+voters) * meanvote)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)

q_movies[['title', 'vote_count', 'vote_average', 'score']].head(20)