import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    data = pd.DataFrame(px.data.gapminder())
    return data