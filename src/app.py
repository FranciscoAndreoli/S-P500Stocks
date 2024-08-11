import streamlit as st
st.set_page_config(layout="wide")
import os
from datetime import datetime
import pandas as pd
import data_processing
from visualizations import view

data_folder = 'src/data'

csv_file_stocks = 'sp500_stocks.csv'
csv_file_index = 'sp500_index.csv'
csv_file_companies = 'sp500_companies.csv'

csv_path_stocks = os.path.join(data_folder, csv_file_stocks)
csv_path_index = os.path.join(data_folder, csv_file_index)
csv_path_companies = os.path.join(data_folder, csv_file_companies)


def main():
    modification_file_time_formated = data_processing.get_file_modification_date(csv_path_index)
    todaysDate = datetime.today().strftime('%Y-%m-%d')

    if modification_file_time_formated is None or todaysDate != modification_file_time_formated:
        modification_file_time_formated = data_processing.download_and_check_modification_date(csv_path_index)

    if modification_file_time_formated is None:
        st.error("Error: Failed to download or access the dataset.")
    else:
        view.initialize_sideBar()
        process_and_visualize_data()

def process_and_visualize_data():
    df_index, df_stocks, df_companies = data_processing.read_files(csv_path_index, csv_path_stocks, csv_path_companies)
    processed_sp_index = data_processing.prepare_sp_line_chart(df_index)
    previous_closing_value = data_processing.get_previous_closing_value(df_index)
    view.create_sp_index_line_chart(processed_sp_index, previous_closing_value)

if __name__ == "__main__":
    main()



    #except FileNotFoundError:
    #    st.error(f"Error: The file '{csv_path}' was not found after download.")
    #except pd.errors.EmptyDataError:
    #    st.error("Error: The downloaded CSV file is empty.")
    #except pd.errors.ParserError:
    #    st.error("Error: The downloaded CSV file is corrupted or improperly formatted.")
    #except Exception as e:
    #    st.error(f"Error: An unexpected error occurred while reading the CSV file - {e}")#