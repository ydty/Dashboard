import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    """Streamlit application
    """

    st.title("Log Dashboard")
    uploaded_file = st.file_uploader("csvファイルを選択してください", type="csv")

    if uploaded_file is not None:

      plot_df = pd.read_csv(uploaded_file)

      fig = px.scatter(plot_df, x="f1", y="f2", color="color", hover_name="name" )
      st.plotly_chart(fig, use_container_width=True)

      st.write(plot_df)

if __name__ == "__main__":
    main()
