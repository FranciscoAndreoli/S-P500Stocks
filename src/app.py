import streamlit as st
st.set_page_config(layout="wide")
import os
from datetime import datetime
import pandas as pd
import data_processing
import processing
from visualizations import view

data_folder = 'src/data'

csv_file_stocks = 'sp500_stocks.csv'
csv_file_index = 'sp500_index.csv'
csv_file_companies = 'sp500_companies.csv'

csv_path_stocks = os.path.join(data_folder, csv_file_stocks)
csv_path_index = os.path.join(data_folder, csv_file_index)
csv_path_companies = os.path.join(data_folder, csv_file_companies)


def main():
    modification_file_time_formated = data_processing.get_file_modification_date(csv_path_stocks)
    todaysDate = datetime.today().strftime('%Y-%m-%d')

    if modification_file_time_formated is None or todaysDate != modification_file_time_formated:
        modification_file_time_formated = data_processing.download_and_check_modification_date(csv_path_stocks)

    if modification_file_time_formated is None:
        st.error("Error: Failed to download or access the dataset.")
    else:
        df_index = data_processing.read_index_file(csv_path_index)
        chart_placeholder = st.empty()
        periodfilter = view.side_bar()
        filter_sp_chart(chart_placeholder, df_index, periodfilter)

def filter_sp_chart(chart_placeholder, df_index, periodfilter):
    if periodfilter == "Histórico":
        processing.process_and_visualize_data(chart_placeholder, df_index)     
    elif periodfilter == "5 Días":
        processing.process_and_visualize_filtered_data(chart_placeholder, df_index, 5)
    elif periodfilter == "1 Mes":
        processing.process_and_visualize_filtered_data(chart_placeholder, df_index, 30)
    elif periodfilter == "6 Meses":
        processing.process_and_visualize_filtered_data(chart_placeholder, df_index, 180)
    elif periodfilter == "1 Año":
        processing.process_and_visualize_filtered_data(chart_placeholder, df_index, 365)

if __name__ == "__main__":
    main()