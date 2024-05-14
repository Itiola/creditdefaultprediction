import streamlit as st

st.title("Smart Credit")
#st.header("I am here")
st.subheader("This Application predicts the credit worthiness of a customer")
#st.text("I am here")

st.selectbox("Gender",["Male","Female"])
st.selectbox("Married",["Yes","No"])
st.number_input("No of Dependent", 0, 10)
st.selectbox("Education (Up to Secondary Level)",["Yes","No"])
st.selectbox("Self Employed",["Yes","No"])
st.number_input("Enter Loan Amount", 0, 1000000000)
st.number_input("Enter Loan Amount Term", 0, 1000)
st.selectbox("Bad Credit History",["Yes","No"])
st.button("Predict Credit Worthiness", type="primary")
