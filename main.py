import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Shane Conway")
    content = """
    Hi, I am Shane! I am an aspiring Software Developer mainly using the programming language Python. I am 25 years old
    and am very passionate and enthusiastic about Software Development and the IT world as a whole! I have worked for
    many companies over the years but I have gotten a taste of what IT/Software Development working environments are 
    like and I don't want to change at all I just want to really kickstart my career as a developer and contribute to
    various projects!
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built using Python. Feel free to contact me!
"""
st.write(content2)


col3, empty_col,col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
