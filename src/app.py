import os
import pandas as pd
import streamlit as st
from kaggle_download import download_dataset

data_folder = 'src/data'
csv_file = 'sp500_stocks.csv'
csv_path = os.path.join(data_folder, csv_file)

if not os.path.exists(csv_path):
    owner_slug = 'andrewmvd'
    dataset_slug = 'sp-500-stocks'
    download_dataset(owner_slug, dataset_slug)

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.dataframe(df.head())
else:
    st.error(f"Error: The file '{csv_file}' was not found.")
