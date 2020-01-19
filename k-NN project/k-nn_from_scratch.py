import numpy as np
from math import sqrt
import warnings
from collections import Counter
import pandas as pd
import random


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total of groups')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(
                np.array(features) - np.array(predict))
        distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / k
    return vote_result, confidence


# Import Data
df = pd.read_csv('football_players.csv')
df = df[['defence', 'midfield', 'attack', 'position']]
full_data = df.values.tolist()
random.shuffle(full_data)


# Data already created
# full_data = [[91, 53, 54, 'defender'], [80, 48, 50, 'defender'], [98, 50, 41, 'defender'], [82, 64, 42, 'defender'], [65, 84, 50, 'midfielder'], [71, 88, 65, 'midfielder'], [59, 89, 56, 'midfielder'], [
#     41, 83, 58, 'midfielder'], [41, 60, 85, 'striker'], [40, 56, 83, 'striker'], [35, 59, 88, 'striker'], [42, 60, 98, 'striker'], [34, 62, 83, 'striker'], [31, 56, 89, 'striker']]
# random.shuffle(full_data)


test_size = 0.5
train_set = {'midfielder': [], 'defender': [], 'striker': []}
test_set = {'midfielder': [], 'defender': [], 'striker': []}
train_data = full_data[:-int(test_size * len(full_data))]
test_data = full_data[-int(test_size * len(full_data)):]
for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote, confidence = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        else:
            print(f'Confidence of: {confidence}')
        total += 1
print(f"Accuracy: {correct / total*100.0} %")
