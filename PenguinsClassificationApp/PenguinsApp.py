# -*- coding: utf-8 -*-
"""
Created on 13.3.2022

@author: Manish Yadav
"""

import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""      
# Penguin Predictions App

## This app will predict the penguin species 

Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
       
 """     )

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
"""
   )

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
        sex = st.sidebar.selectbox('Sex',( 'male', 'female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6, 43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
        flipper_length_mm = st.sidebar.slider('flipper length (mm)', 172.0, 231.0, 201.0)
        body_mass_g = st.sidebar.slider('Body mass (grams)', 2700.0, 6300.0, 4207.0)
        data = {'island': island,
                'bill_length_mm':bill_length_mm,
                'bill_depth_mm':bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex
            }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()


### Reading data from penguins_cleaned.csv file

penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df, penguins], axis=0)

### encoding of ordinal features
encode = ['sex', 'island']

for i in encode:
    dummy = pd.get_dummies(df[i], prefix=i)
    df = pd.concat([df, dummy], axis=1)
    del df[i]        
df = df[:1]

st.subheader(('User input features'))

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)
    
### Reading saved classification model
Dir = 'D:/Work/Programming/Projects/streamlit/PenguinsClassificationApp'
load_clf = pickle.load(open(os.path.join(Dir, 'Penguins_clf.pkl'), 'rb'))

### using this model to make predications
prediction = load_clf.predict(df)
predication_proba = load_clf.predict_proba(df)


st.subheader('Prediction')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction probability')
st.write(predication_proba)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



