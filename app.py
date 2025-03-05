   
import streamlit as st
 
st.set_page_config(page_title="growth mindset project", page_icon="★")

st.title("Growth Mindset Challange: Web App with Streamlit")

st.header("🚀Welcome to your Growth Journy!")
st.write("Embrace challange,leaarn from mistakes,and unlock your full potential.This ai-powered app helps you build a growth mindset withreflection,challenges,and achievements!")

st.header("💡 Today's Growth Mindset Quote")
st.write("Sucess is not final,failure is not fetal:it is the courage to continue that counts.")

st.header("🔧 What's your Challange Today?")
user_input= st.text_input("Describe a challange you're facing:")

if user_input:
    st.success(f"You are facing:{user_input}. Keep pushing forword towerds your goal!")
else:
    st.warning("Tell us about your challange to get started!")
    
st.header("Reflect o your Learning")
reflection =st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great Insight! Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulites")
    
    st.header("🏆 Celebrate Your Wins!")
    acheivment = st.text_input("Share something you've recently accomplished:")
    
    if acheivment:
        st.success(f"🛩️ Amazing! You achived:{acheivment}")
    else:
        st.info("Big or small , every achivement counts! Share one now 😍")
        
        st.write(" - - -")
        st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination!★ ")
        st.write("🤜🏻 Created by Aqsa Qayyum")