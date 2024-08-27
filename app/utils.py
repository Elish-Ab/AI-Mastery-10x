import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def plot_time_series(data):
    """Plot time series for GHI, DNI, DHI."""
    fig, ax = plt.subplots()
    ax.plot(data['Timestamp'], data['GHI'], label='GHI')
    ax.plot(data['Timestamp'], data['DNI'], label='DNI')
    ax.plot(data['Timestamp'], data['DHI'], label='DHI')
    plt.xlabel('Timestamp')
    plt.ylabel('Irradiance (W/m²)')
    plt.title('Solar Radiation Over Time')
    plt.legend()
    st.pyplot(fig)

def plot_histograms(data):
    """Plot histograms for key variables."""
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    sns.histplot(data['GHI'], bins=30, ax=ax[0])
    ax[0].set_title('Distribution of GHI')
    sns.histplot(data['DNI'], bins=30, ax=ax[1])
    ax[1].set_title('Distribution of DNI')
    sns.histplot(data['DHI'], bins=30, ax=ax[2])
    ax[2].set_title('Distribution of DHI')
    st.pyplot(fig)

def plot_correlation_heatmap(data):
    """Plot a heatmap to show correlations."""
    corr = data[['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, ax=ax)
    plt.title('Correlation Matrix')
    st.pyplot(fig)


