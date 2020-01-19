import numpy as np
from sklearn import preprocessing, model_selection, neighbors, svm
import pandas as pd

df = pd.read_csv('football_players2.txt')
df.replace('?', -99999, inplace=True)
df.drop(['name'], 1, inplace=True)

X = np.array(df.drop(['position'], 1))
y = np.array(df['position'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.2)
clf = svm.SVC()

clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = {'defender': np.array([[81, 36]]),
                    'striker': np.array([[22, 85]])
                    }

for example in example_measures.items():
    prediction = clf.predict(example[1])
    print(f'Prediction of {example[0]} was: {prediction}')

another_test = np.array([[11, 99]])
print(clf.predict(another_test))
