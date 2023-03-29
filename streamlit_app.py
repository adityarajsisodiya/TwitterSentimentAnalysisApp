import streamlit as st
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

file=open("twitter_model.pkl","rb")
model=pickle.load(file)

#method to predict reaction based on tweet
def analyse_tweet(text):  
        result=model.predict([tweet])
        return result[0]
st.title("Twitter Sentiment Analysis App")
tweet=st.text_input(label="Write Tweet To Analyse it")
button=st.button(label="Submit")
if(button):
    result=analyse_tweet(tweet)
    if(result==0):
        st.write("negative tweet")
    elif(result==1):
        st.write("positive tweet")
    else:
        st.write("internal error")
