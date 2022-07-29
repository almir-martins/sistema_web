import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(
        uploaded_file,
        index_col=0,
        names=["Open", "High", "Low", "Close", "Tick", "Volume"],
        encoding="utf-16",
    )

    st.title("Lendo csv!")
    st.write(df)
