import streamlit as st
import joblib
import pandas as pd

# Load the Model
@st.cache_resource
def load_model():
    # Make sure this matches your saved filename exactly
    model = joblib.load('cmapss_rf_model_rmse_19.joblib')
    return model

model = load_model()

# App Title
st.title("✈️ Jet Engine RUL Predictor")
st.write("""
**Project:** CMAPSS Jet Engine Maintenance
**Model:** Random Forest (RMSE ~19)
         
Upload sensor data to predict the Remaining Useful Life (RUL) of the engines.
""")

# File Uploader
uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])

if uploaded_file is not None:
    input_data = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview")
    st.dataframe(input_data.head())

    if st.button("Predict RUL"):
        try:
            predictions = model.predict(input_data)
            results = input_data.copy()
            results['Predicted_RUL'] = predictions
            
            st.success("Prediction Complete!")
            st.write("### Prediction Results")
            st.dataframe(results[['Predicted_RUL']].style.highlight_min(axis=0))
            
            # Simple Graph
            st.line_chart(results['Predicted_RUL'])
            
        except Exception as e:
            st.error(f"Error: {e}")