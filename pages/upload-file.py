import streamlit as st
import pandas as pd

st.markdown("Predict results on csv file")
st.sidebar.markdown("Predict results on csv file")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    try:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe[1:5])
    except:
        st.warning("you need to upload a csv file.")

    
    