import streamlit as st
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Streamlit Crash course")
st.header("Simple Header")
st.subheader("Another sub header")
st.sidebar.header("Example de Side Bar")
st.sidebar.text("Hello")
st.text("For a simple text")
st.markdown("#### A Markdown ")

@st.cache
def load_data(name):
    """ Load dataset from seaborn
        See the available list here : https://github.com/mwaskom/seaborn-data
    """
    return seaborn.load_dataset(str(name))

#utilisation de la fonction load_data()
df = load_data(iris)
