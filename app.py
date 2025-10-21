 import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Car Risk Data Visualization')

# Load the data
try:
    data = pd.read_csv("carRisk - futuro.csv")
    st.write("Raw Data:")
    st.dataframe(data)

    # Display histogram of 'edad'
    st.write("Histogram of Edad:")
    fig, ax = plt.subplots()
    ax.hist(data['edad'], bins=10)
    st.pyplot(fig)

except FileNotFoundError:
    st.error("Error: 'carRisk - futuro.csv' not found.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Car Risk Data Visualization')

# Load the data
try:
    data = pd.read_csv("carRisk - futuro.csv")
    st.write("Raw Data:")
    st.dataframe(data)

    # Display histogram of 'edad'
    st.write("Histogram of Edad:")
    fig, ax = plt.subplots()
    ax.hist(data['edad'], bins=10)
    st.pyplot(fig)

except FileNotFoundError:
    st.error("Error: 'carRisk - futuro.csv' not found.")
