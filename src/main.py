import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Layout (Main)
st.markdown("## plotly_chart")
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])

# Plot
st.plotly_chart(fig, use_container_width=True)

# Layout (Sidebar)
st.sidebar.markdown("## 設定項目や検索項目など")
