import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px


def app():
    st.title('Data Satisfaction')

    st.header('Here is sample data from the cleaned table')
    clean_data_df = pd.read_csv("./data/telecom_user_satisfaction_data.csv")
    st.dataframe(clean_data_df)
