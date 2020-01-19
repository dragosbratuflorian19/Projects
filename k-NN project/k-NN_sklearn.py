"""
This script is will predict the position of a football player, based on his Defence/Midfield/Attack ratings. It will be used the sklearn module
"""

import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

# Load the csv file into a pandas dataframe
df = pd.read_csv('football_players.csv')

# Splitting the dataframe into data to calculate (ratings) and expected outcome (position)
ratings_ar = np.array(df.drop(['position', 'name'], axis=1))
position_ar = np.array(df['position'])

# making the splitting between data for training and data for testing
ratings_train, ratings_test, position_train, position_test = model_selection.train_test_split(
    ratings_ar, position_ar, test_size=0.2)
# Creating the k-NN classifier tool
knn_tool = neighbors.KNeighborsClassifier(n_jobs=-1)

# Fitting the prepared data
knn_tool.fit(ratings_train, position_train)

# Getting the accuracy after the classification done
accuracy = knn_tool.score(ratings_test, position_test)
print(f'Accuracy is: {accuracy*100} %')

# Checking the model with an example
example_ratings = np.array(
    [[13, 66, 89], [54, 66, 43], [87, 87, 87], [11, 11, 11]])
example_names = np.array([['striker', 'Drogba'], ['midfielder', 'Iulian'], [
    'midfielder', 'Bratu'], ['defender', 'Vlad']])
example_ratings = example_ratings.reshape(len(example_ratings), -1)
predictions = knn_tool.predict(example_ratings)
for i in range(len(example_ratings)):
    print(f'{example_names[i, 1]} was predicted {predictions[i]}, he is actually {example_names[i, 0]}')
