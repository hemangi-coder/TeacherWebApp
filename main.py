import streamlit as st
import pandas as pd
from PIL import Image

@st.cache
def get_data():
    path = r'StudentNamesList.csv'
    return pd.read_csv(path)
df = get_data()

names = df['Student Name'].drop_duplicates()
name_choice = st.selectbox('Select your Name:', names)

subject = df['Subject'].drop_duplicates()
subject_choice = st.selectbox('Select your Subject:', subject)

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
