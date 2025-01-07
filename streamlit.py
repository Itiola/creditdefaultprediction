import streamlit as st
import numpy as np
import pickle

st.title("Smart Credit")
#st.header("I am here")
st.subheader("This Application predicts the credit worthiness of a customer")

# Define feature names and input widgets
features = {}
features["Dependent_No"] = st.number_input("Number of Dependents", min_value=0)
features["Loan_Amount"] = st.number_input("Loan Amount")
features["Loan_Amount_Term"] = st.number_input("Loan Term (Months)")
features["Applicant_Income"] = st.number_input("Applicant Income")
features["CoApplicant_Income"]=  st.number_input("Co-Applicant Income", min_value=0)
features["Gender"] = st.selectbox("Gender", ["Male", "Female"])
features["Married"] = st.selectbox("Marital Status", ["Married", "Single"])
features["Education"] = st.selectbox("Education Level", ["Graduate", "Undergraduate"])
features["Self_Employed"] = st.selectbox("Self-Employed", ["Yes", "No"])
features["Credit_History"] = st.selectbox("Credit History", ["Yes", "No"])

# Convert selectbox selections to numerical values for model input
features["Gender"] = 1 if features["Gender"] == "Male" else 0
features["Married"] = 1 if features["Married"] == "Married" else 0
features["Education"] = 1 if features["Education"] == "Graduate" else 0
features["Self_Employed"] = 1 if features["Self_Employed"] == "Yes" else 0
features["Credit_History"] = 1 if features["Credit_History"] == "Yes" else 0

# Define a function to prepare features for prediction
def prepare_features_for_prediction(features):
  """
  This function extracts feature values from the dictionary and reshapes them
  into a 2D array suitable for model prediction.
  """
  feature_values = list(features.values())  # Extract feature values as list
  return np.array(feature_values).reshape(1, -1)  # Reshape to 2D array (single row)

# Load credit model from pickle file
with open('smartcreditmodel.pkl', 'rb') as pickle_file:
  model = pickle.load(pickle_file)

# Predict loan default when the user clicks the submit button
if st.button("Submit Application"):
  features_for_prediction = prepare_features_for_prediction(features)
  prediction = model.predict(features_for_prediction)

  # Display prediction result
  st.write(f"**Prediction:** {prediction[0]}")  # Assuming prediction is a probability
else:
  st.write("Please fill out all fields with valid values.")
