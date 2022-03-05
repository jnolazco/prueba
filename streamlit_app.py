import streamlit as st
import pandas as pd

st.write("Adsoft Pandas:")
st.write(pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40]
}))
