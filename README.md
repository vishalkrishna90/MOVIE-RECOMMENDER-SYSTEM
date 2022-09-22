
# CONTENT BASED MOVIE RECOMMENDER SYSTEM

This is a **Movie Recommender System Project**, in which I tried to build a **Recommender Model** which helps
we can check **Movie Recommendations**, You just need to click on the **Recommend Button**, You will get the 6 recommended movies
based on the content, You can click on the below link and go to the web app to check how it is looking and working.

[Go To The Web App](https://movierecommendersystem123.herokuapp.com/)

![Movie Recommender System](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_1.png)

**Author = Vishal Kumar Mridha**

**Domain = Entertainment**

**Level = Intermediate**

**Project Type = End To End Project**

## Table Of Content
- Problem Statement
- Data Collection 
- Data Descreption 
- Data Preprocessing
- Model Building
- Make Pickle File
- Create New Enviornment
- Create Web App With Streamlit
- Upload All Files In Github repository
- Deploy Model On Heroku

**Web App Overview**

![Web App 1](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_2.png)
![Web App 2](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_3.png)
![Web App 3](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_4.png)
## Problem Statement

As we know, everyone in this world loves to watch movies, but it is a bit difficult to find a similar type of movie without any recommendation system. That's why I tried to build a movie recommendation system with the help of **Cosine Similarity** and **TMDB Movie API**.
## Data Collection
I got data from kaggle, first I downloaded dataset in my local storage then uploaded in jupyter notebook

```
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')
```
**Data Overview**

![Data Overview 1](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Overview_1.png)
![Data Overview 1](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Overview_2.png)

## Data Description

For this project we imported two datasets, first dataset has 4803 rows and 20 columns and second dataset has 4803 rows and 4 columns.

[Dataset Link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
## Data Preprocessing
In this step first I merged both datasets and took only important columns and then checked whether there are any null and duplicate values present or not, and I found there are some null values present but no duplicate values. I dropped all null values.

After that, I created some functions to extract only useful data from the column and then extracted all useful data to build our model.


## Model Building
In this step, first I vectorized all values with the help of
Count Vectorizer and then I used Cosine Similarity to build our recommendation model

## Make Pickle File
After building the model, I created a Pickle file for deployment of web app

```
import pickle as pkl
pkl.dump(similarity,open('sim.pkl','wb'))
```

## Create New Enviornment
After making pickle file I created new virtual environment for the 
project and install required libraries and created web app in VS Code IDE

```
conda create -p movierecommend python==3.9 -y
```

```
pip install streamlit numpy pandas sklearn requests matplotlib
``` 

## Create Web App With Streamlit
After installing all required libraries and dependencies I created web app 

![Web App 1](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_1.png)

## Upload All Files In Github repository

After creating web app I uploaded all files in github repository by git CLI and git LFS
```
git lfs install
```
```
git lfs track "*.pkl"
```

```
git add .gitattributes
```

```
git add files_name
```

```
git commit -m  "about the commit"
```

```
git push origin main
```

## Deploy Model On Heroku

In the end, I deployed the model on Heroku, so that anybody can use the web app

[Movie Recommender System Web App](https://movierecommendersystem123.herokuapp.com/)
![Movie Recommender System 1](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_2.png)
![Movie Recommender System 2](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_3.png)
![Movie Recommender System 3](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/Movie_4.png)

## Deployment Requirement Tools 

![Deploy](https://github.com/vishalkrishna90/MOVIE-RECOMMENDER-SYSTEM/blob/main/Images/st_im.png)

 - [Streamlit](https://streamlit.io/)
 - [Github Account](https://github.com/)
 - [Heroku Account](https://dashboard.heroku.com/apps)
 - [Visual Studio Code](https://code.visualstudio.com/)
 - [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


