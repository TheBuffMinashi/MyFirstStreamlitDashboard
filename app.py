import streamlit as st
import pandas as pd
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

st.title('A Simple Streamlit Web App')
name = st.text_input('Enter YouTube playlist URL here:', '')

df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(df)
