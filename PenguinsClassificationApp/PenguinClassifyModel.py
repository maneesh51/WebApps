# -*- coding: utf-8 -*-
"""
Created on 13.03.2022

@author: Manish Yadav
"""

import pandas as pd
import os

Dir = 'D:/Work/Programming/Projects/streamlit/PenguinsClassificationApp'
penguins = pd.read_csv(os.path.join(Dir, 'penguins_cleaned.csv'))

df = penguins.copy()

#predicting the species of the penguin
target = 'species'

#features
encode = ['sex', 'island']

for i in encode:
    dummy = pd.get_dummies(df[i], prefix=i)
    df = pd.concat([df, dummy], axis=1)
    del df[i]

# labelling the species
target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}

def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)


## Separating X and  Y
X = df.drop('species', axis=1)
Y = df['species']

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
clf.fit(X, Y)

### Saving model with pickle
import pickle

pickle.dump(clf, open(os.path.join(Dir, 'Penguins_clf.pkl'), 'wb'))





















