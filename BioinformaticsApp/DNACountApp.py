# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:17:06 2022

@author: genxm
"""
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import os

Dir = 'D:/Work/Programming/Projects/streamlit/BioinformaticsApp/'
image = Image.open(os.path.join(Dir,'DNA_cartoon.jpg'))

st.image(image, use_column_width=True)

st.write("""
# DNA nucleotide count web app

This app count the nucleotide composition of query DNA.


""")

st.header('Enter DNA Sequence')
sequence_input = ">DNA Query \nGCCTCTAGCAACAATAAGTATTAGAGGTA\
    ATGCCTGCCCAGTGACACTGTTAAACGGCCGCGGTATCCTAACCGTGCAAAGGTAG\
        CGTAATCACTTGTCTTTTAAATAAAGACTAGAATG\
AATGGCCAAACGAGGTTCCACCTGTCTCTTACAAACAATCAGTGAAATTGGTCTTCCCGT\
GCAAAAGCGGGAATAACACTATAAGACGAGAAGACCCTGTGGAACTTCAAATATAAATCA\
ACTATTATATTTACCACCCTAAAGACTTATAATTAACTAGTTCTGATCCATATTTTTGGT\
TGGGGTGACCTCGGAGTAAAACAAAACCTCCGAAAAAAGAACATATTTTCTTAACCTAGA\
TTTACAACTCAAAGCGCCAACGGCAAAATGATCCAATATATTTGATCAACGAACCAAGCT\
ACCCCAGGGATAACAGCGCAATCCCATCCTAGAGTTCCTATCGACGATGGGGTTTACGAC\
CTCGATGTTGGATCAGGACATCCTGATGGTGCAACCGCTATCAAGGGTTCGTTTGTTCAA\
CGATTAATAGTCCTACGTGAT"


sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
        ****
         """)
         
st.header('Input(DNA Query)')
sequence

st.header('DNA nucleotide count')

st.subheader('1. Print Dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
                ('A', seq.count('A')),
                ('T', seq.count('T')),
                ('G', seq.count('G')),
                ('C', seq.count('C'))
                ])
    
    return d


X = DNA_nucleotide_count(sequence)

X

### print text
st.subheader('2. Print text')
st.write('There are '+str(X['A'])+ 'adenine (A)')
st.write('There are '+str(X['T'])+ 'thymine (T)')
st.write('There are '+str(X['G'])+ 'guanine (G)')
st.write('There are '+str(X['C'])+ 'cytosine (C)')


### Display dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})
st.write(df)


### 4. Display bar plot using Altair

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(x='nucleotide', y='count')
p = p.properties(width=alt.Step(120))
st.write(p)






























