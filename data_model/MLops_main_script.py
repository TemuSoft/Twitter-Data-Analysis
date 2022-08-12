import streamlit as st
import pandas as pd
import plotly.express as px
import deploy_on_graph_module
import load_data_module 
st.set_page_config(layout = "wide")



df= load_data_module.load_data()

st.title("10 Academy MLops Project on National Statistics Data")
page = st.sidebar.selectbox('Select The Page You Want to see: ',
  ['Country data','Continent data'])


graph=deploy_on_graph_module.load_graph(page,df)
st.write(graph)