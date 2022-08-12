

import streamlit as st
import pandas as pd
import plotly.express as px



def load_graph(page,df):
  if page == 'Country data':
  ## Countries
    clist = df['country'].unique()
    country = st.selectbox("Select a country:",clist)
    col1, col2 = st.columns(2)
    fig = px.line(df[df['country'] == country], 
      x = "year", y = "gdpPercap",title = "GDP per Capita")
 
    column1= col1.plotly_chart(fig,use_container_width = True)
    fig = px.line(df[df['country'] == country], 
      x = "year", y = "pop",title = "Population Growth")
  
    column2= col2.plotly_chart(fig,use_container_width = True)
    return column1, column2
  else:
    ## Continents
    contlist = df['continent'].unique()
 
    continent = st.selectbox("Select a continent:",contlist)
    col1,col2 = st.columns(2)
    fig = px.line(df[df['continent'] == continent], 
      x = "year", y = "gdpPercap",
      title = "GDP per Capita",color = 'country')
  
    column11= col1.plotly_chart(fig)
    fig = px.line(df[df['continent'] == continent], 
      x = "year", y = "pop",
      title = "Population",color = 'country')
  
    column22= col2.plotly_chart(fig, use_container_width = True)
    return column11, column22