import pandas as pd
import numpy as np

#1. load data
ratings = pd.read_csv('resources/u.rating', sep='\t', header=0)
print(ratings)

#2. rename
print(ratings.columns)
ratings.rename(columns={ratings.columns[0]:'id'})
print(ratings.head())

#3. map
ratings['timestamp'] = ratings['timestamp'].map(lambda x : x/1000)
print(ratings)

# [function(x) for x in list_of_x]


