import streamlit as st
import numpy as np
import pandas as pd
import sys
import os
import plotly.express as px

# from sklearn import datasets


def app():
    st.title('Data Overview')

    clean_data_df = pd.read_csv("../data/telecom_cleaned_data.csv")

    st.header('Here we have An Overview of our data set')
    st.write(clean_data_df)
    st.header("here are The top Handsets found in dataset")
    st.write(clean_data_df['Handset Type'].value_counts())
    # st.bar_chart(
    #     clean_data_df['Handset Type'].value_counts().head(10))

    fig = px.bar(clean_data_df['Handset Type'].value_counts().rename_axis(
        'Handset Type').reset_index(name='counts').head(10), x='Handset Type', y='counts')
    st.plotly_chart(fig)
    # fig.show()
    top_handset_manufacturers = clean_data_df['Handset Manufacturer'].value_counts(
    ).head(3)
    top_handset_manufacturers = clean_data_df[clean_data_df["Handset Manufacturer"].isin(
        top_handset_manufacturers.index.tolist())]
    top_handsets = top_handset_manufacturers['Handset Type'].groupby(
        clean_data_df['Handset Manufacturer']).apply(lambda x: x.value_counts().head(5))
    st.header("here are The top Handsets by manufacturer found in dataset")
    st.dataframe(top_handsets)
    st.header("here are The top Numbers With the Top number of sessions")
    number_of_xdr = clean_data_df.groupby('MSISDN/Number')['MSISDN/Number'].agg(
        'count').reset_index(name='Bearer Id').sort_values(by='Bearer Id', ascending=False)
    number_of_xdr.rename(
        columns={number_of_xdr.columns[1]: 'number of xDR sessions'}, inplace=True)
    st.dataframe(number_of_xdr.head(10))
    fig = px.bar(number_of_xdr.head(10), x='MSISDN/Number',
                 y='number of xDR sessions')
    fig.update_layout(xaxis_type='category')
    st.plotly_chart(fig)
    st.header("here are The top Numbers With the Top total duration of sessions")
    sum_duration_of_sessions = clean_data_df.groupby(
        'MSISDN/Number').agg({'Dur (ms)': 'sum'}).sort_values(by='Dur (ms)', ascending=False)
    sum_duration_of_sessions.rename(columns={
                                    sum_duration_of_sessions.columns[0]: 'duration of xDR sessions (total)'}, inplace=True)
    sum_duration_of_sessions['duration of xDR sessions (total)'] = sum_duration_of_sessions['duration of xDR sessions (total)'].astype(
        "int64")
    st.dataframe(sum_duration_of_sessions.head(10))
    st.header("here are The top Numbers With the Top avarage duration of sessions")
    avg_duration_of_sessions = clean_data_df.groupby(
        'MSISDN/Number').agg({'Dur (ms)': 'mean'}).sort_values(by='Dur (ms)', ascending=False)
    avg_duration_of_sessions.rename(columns={
                                    avg_duration_of_sessions.columns[0]: 'duration of xDR sessions (AVG)'}, inplace=True)
    avg_duration_of_sessions
    st.dataframe(avg_duration_of_sessions.head(10))
    st.header("here are The top Numbers With the Top Total Data Used")
    data_volumes = clean_data_df.groupby('MSISDN/Number')[['Total UL (Bytes)', 'Total DL (Bytes)',
                                                           'Total Data Volume (Bytes)']].sum().sort_values(by='Total Data Volume (Bytes)', ascending=False)
    data_volumes['Total Data Volume (Bytes)'] = data_volumes['Total Data Volume (Bytes)'].astype(
        "int64")
    data_volumes['Total DL (Bytes)'] = data_volumes['Total DL (Bytes)'].astype(
        "int64")
    data_volumes['Total UL (Bytes)'] = data_volumes['Total UL (Bytes)'].astype(
        "int64")
    st.dataframe(data_volumes)

    fig = px.histogram(data_volumes, x="Total Data Volume (Bytes)")
    st.plotly_chart(fig)