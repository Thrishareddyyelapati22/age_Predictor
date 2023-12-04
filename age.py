import streamlit as st
import datetime
st.title("Age Predictor")
name=st.text_input("Enter your Name Here")
age=st.number_input("Enter your age")
gender=st.radio("Enter your gender",["Male","Female","Other"])
Address=st.text_area("Enter your address")
x=st.button("Submit")
if x:
	if age>=18:
		st.success("You are eligible to vote")
	else:
		st.error("Sorry,Not Eligible to vote")
