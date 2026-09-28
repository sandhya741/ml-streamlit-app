import streamlit as st
import joblib
model=joblib.load("mode.pkl")
st.title("student marks prediction")
st.write("enter students study hrs ")
study_hours=st.number_input("study_hours",min_value=0.0,max_value=15.0,value=5.0)
attendence=st.number_input("attendenec",min_value=0.0,max_value=100.0,value=75.0)
if(st.button('predict marks')):
    input_data=[[study_hours,attendence]]
    pred=model.predict(input_data)
    st.success(f"predicted marks:{pred[0]:.2f}")