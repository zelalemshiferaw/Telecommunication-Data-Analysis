import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px


def app():
    st.title('Data Experience')
    clean_data_df = pd.read_csv("../data/telecom_cleaned_data.csv")

    tellco_exprience_df = clean_data_df[['MSISDN/Number', 'Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)',
                                         'Avg Bearer TP UL (kbps)', 'TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)', 'Handset Type']]
    tellco_exprience_df['Total Avg RTT (ms)'] = tellco_exprience_df['Avg RTT DL (ms)'] + \
        tellco_exprience_df['Avg RTT UL (ms)']
    tellco_exprience_df['Total Avg Bearer TP (kbps)'] = tellco_exprience_df['Avg Bearer TP DL (kbps)'] + \
        tellco_exprience_df['Avg Bearer TP UL (kbps)']
    tellco_exprience_df['Total TCP Retrans. Vol (Bytes)'] = tellco_exprience_df['TCP DL Retrans. Vol (Bytes)'] + \
        tellco_exprience_df['TCP UL Retrans. Vol (Bytes)']
    tellco_exprience_df = tellco_exprience_df[[
        'MSISDN/Number', 'Total Avg RTT (ms)', 'Total Avg Bearer TP (kbps)', 'Total TCP Retrans. Vol (Bytes)', 'Handset Type']]
    tellco_exprience_df1 = tellco_exprience_df.groupby(
        'MSISDN/Number').agg({'Total Avg RTT (ms)': 'sum', 'Total Avg Bearer TP (kbps)': 'sum', 'Total TCP Retrans. Vol (Bytes)': 'sum', 'Handset Type': [lambda x: x.mode()[0]]})  # ' '.join(x)
    tellco_exprience_df = pd.DataFrame(columns=[
        "Total Avg RTT (ms)",
        "Total Avg Bearer TP (kbps)",
        "Total TCP Retrans. Vol (Bytes)",
        "Handset Type"])

    tellco_exprience_df["Total Avg RTT (ms)"] = tellco_exprience_df1["Total Avg RTT (ms)"]['sum']
    tellco_exprience_df["Total Avg Bearer TP (kbps)"] = tellco_exprience_df1["Total Avg Bearer TP (kbps)"]['sum']
    tellco_exprience_df["Total TCP Retrans. Vol (Bytes)"] = tellco_exprience_df1[
        "Total TCP Retrans. Vol (Bytes)"]['sum']
    tellco_exprience_df["Handset Type"] = tellco_exprience_df1["Handset Type"]['<lambda>']
    option = st.selectbox(
        'Top 10 of the top, bottom and most frequent Datas Based on',
        ('Total Avg RTT (ms)', 'Total Avg Bearer TP (kbps)', 'Total TCP Retrans. Vol (Bytes)'))

    # if option == 'Total Avg RTT (ms)':
    data = tellco_exprience_df.sort_values(option, ascending=False)
    highest = data.head(10)[option]
    lowest = data.tail(10)[option]
    most = tellco_exprience_df[option].value_counts().head(10)
    st.header("Highest")
    highest = highest.reset_index('MSISDN/Number')
    fig = px.bar(highest, x='MSISDN/Number', y=option)
    fig.update_layout(xaxis_type='category')
    st.plotly_chart(fig)
    st.header("Lowest")
    lowest = lowest.reset_index('MSISDN/Number')
    fig = px.bar(lowest, x='MSISDN/Number', y=option)
    fig.update_layout(xaxis_type='category')
    # fig = px.pie(lowest, names='MSISDN/Number', values=option)
    st.plotly_chart(fig)
    # most = most.reset_index('MSISDN/Number')
    # fig = px.pie(most, names='MSISDN/Number', values=option)
    # st.plotly_chart(fig)
    st.header("Most")
    st.dataframe(most)
    # name = 'number of xDR Sessions'
    # elif option == 'Total Avg Bearer TP (kbps)':
    #     data = clean_data_df.sort_values('Dur (ms)', ascending=False).head(10)
    #     # name = 'Dur (ms)'
    # elif option == 'Total TCP Retrans. Vol (Bytes)':
    #     data = clean_data_df.sort_values(
    #         'Total Data Volume (Bytes)', ascending=False).head(10)
    # name = 'Total Data Volume (Bytes)'

    # st.plotly_chart(fig)