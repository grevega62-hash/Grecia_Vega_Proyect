import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de autos 🚗")

# leer datos
df = pd.read_csv('vehicles_us.csv')

# histograma
if st.checkbox('Mostrar histograma'):
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig)

# dispersión
if st.checkbox('Mostrar dispersión'):
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig)