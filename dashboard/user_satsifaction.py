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
    clean_data_df = clean_data_df[['MSISDN/Number', 'Bearer Id', 'Dur (ms)', 'Total Data Volume (Bytes)', 'Social Media Data Volume (Bytes)', 'Google Data Volume (Bytes)',
                                   'Email Data Volume (Bytes)', 'Youtube Data Volume (Bytes)', 'Netflix Data Volume (Bytes)',
                                   'Gaming Data Volume (Bytes)', 'Other Data Volume (Bytes)']]
    clean_data_df = clean_data_df.groupby(
        'MSISDN/Number').agg({'Bearer Id': 'count', 'Dur (ms)': 'sum', 'Total Data Volume (Bytes)': 'sum'})
    clean_data_df = clean_data_df.rename(
        columns={'Bearer Id': 'number of xDR Sessions'})
    option = st.selectbox(
        'Top 10 Numbers (Users) with highest',
        ('number of xDR Sessions', 'number of Duration', 'total Data Volume'))

    if option == 'number of xDR Sessions':
        data = clean_data_df.sort_values(
            'number of xDR Sessions', ascending=False).head(10)
        name = 'number of xDR Sessions'
    elif option == 'number of Duration':
        data = clean_data_df.sort_values('Dur (ms)', ascending=False).head(10)
        name = 'Dur (ms)'
    elif option == 'total Data Volume':
        data = clean_data_df.sort_values(
            'Total Data Volume (Bytes)', ascending=False).head(10)
        name = 'Total Data Volume (Bytes)'
    data = data.reset_index('MSISDN/Number')
    fig = px.pie(data, names='MSISDN/Number', values=name)
    st.plotly_chart(fig)


    st.dataframe(data)