import streamlit as st
import pandas as pd

@st.cache
def get_data():
    path = r'StudentNamesList.csv'
    return pd.read_csv(path)
df = get_data()

names = df['Student Name'].drop_duplicates()
name_choice = st.selectbox('Select your Name:', names)

subject = df['Subject'].drop_duplicates()
subject_choice = st.selectbox('Select your Subject:', subject)