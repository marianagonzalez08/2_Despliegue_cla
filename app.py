import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model and preprocessing objects
try:
    with open('modelo-cla.pkl', 'rb') as f:
        modelo_knn, min_max_scaler, variables, labelencoder = pickle.load(f)
except FileNotFoundError:
    st.error("Error: modelo-cla.pkl not found. Make sure the model file is uploaded.")
    st.stop()

st.title('Predicción de Riesgo de Carro')

# Input fields for carRisk data
edad = st.slider('Edad', min_value=data['edad'].min(), max_value=data['edad'].max(), value=int(data['edad'].mean()), step=1)
tipoCarro_options = ['combi', 'sport', 'family', 'minivan'] # Assuming these are the possible car types
tipoCarro = st.selectbox('Tipo de Carro', tipoCarro_options)

# Prepare data for prediction
input_data = pd.DataFrame([[edad, tipoCarro]], columns=['edad', 'tipoCarro'])

# Apply the same preprocessing steps as in the notebook
# Create dummy variables
input_data_processed = pd.get_dummies(input_data, columns=['tipoCarro'], dtype=int, drop_first=False)

# Reindex columns to match the training data, filling missing with 0
input_data_processed = input_data_processed.reindex(columns=variables, fill_value=0)

# Normalize the 'edad' column using the loaded scaler
# Ensure 'edad' column is present before scaling
if 'edad' in input_data_processed.columns:
    # Reshape the data before transforming
    input_data_processed[['edad']] = min_max_scaler.transform(input_data_processed[['edad']].values.reshape(-1, 1))
else:
    st.error("Error: 'edad' column not found after processing.")
    st.stop()

# Make prediction
try:
    prediction_numeric = modelo_knn.predict(input_data_processed)
    prediction_text = labelencoder.inverse_transform(prediction_numeric)
    st.write(f'La predicción de riesgo es: **{prediction_text[0]}**')
except Exception as e:
    st.error(f"Error during prediction: {e}")
