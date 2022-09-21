import streamlit as st
import pandas as pd
import numpy as np
import warnings as was
was.filterwarnings('ignore')
import pickle as pkl
import requests


similarity  = pkl.load(open('sim.pkl','rb'))
movies = pd.read_csv('https://raw.githubusercontent.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/main/filtered_movies.csv')


def fetch_postor(moive_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(moive_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend_movie(movie):
    m_i = movies[movies['title'] == movie].index[0]
    dis = similarity[m_i]
    m_l = sorted(list(enumerate(dis)), reverse=True, key = lambda x: x[1])[1:7]
    
    rec_movie = []
    rec_mo_pos = []
    for i in m_l:
        movie_id = movies.iloc[i[0]].id
        rec_movie.append(movies.iloc[i[0]].title)
        rec_mo_pos.append(fetch_postor(movie_id))
    return rec_movie,rec_mo_pos

st.title('MOVIE RECOMMENDER SYSTEM')
st.image('mrs.jpeg')
datas = st.selectbox('SELECT MOVIES:', movies['title'].values)

btn = st.button('Recommend')

if btn:
    names,posters = recommend_movie(datas)
    col1,col2,col3 = st.columns(3)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])

    col4,col5,col6  = st.columns(3)
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
