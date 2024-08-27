import streamlit as st
import pandas as pd
import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils import load_data, plot_time_series, plot_histograms, plot_correlation_heatmap

st.title("Solar Radiation Data Dashboard")

# Sidebar for selecting region
st.sidebar.header("Select Region")
region = st.sidebar.selectbox("Choose a region:", ("Region 1", "Region 2", "Region 3"))

# Load the data based on user selection
data_path = f"data/{region.lower().replace(' ', '_')}.csv"  # Adjust the path to match your CSV filenames
data = load_data(data_path)

# Show raw data option
if st.checkbox("Show raw data"):
    st.write(data.head())

# Time series plot
st.subheader("Time Series Analysis")
plot_time_series(data)

# Histograms
st.subheader("Distribution of Variables")
plot_histograms(data)

# Correlation Heatmap
st.subheader("Correlation Analysis")
plot_correlation_heatmap(data)