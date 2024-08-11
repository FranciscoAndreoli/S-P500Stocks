import pandas as pd
import kaggle_download
from datetime import datetime, timedelta
import os
import streamlit as st

def get_file_modification_date(path):
    try:
        modification_file_time = os.path.getmtime(path)
        dt_m = datetime.fromtimestamp(modification_file_time)
        return dt_m.strftime("%Y-%m-%d")
    except FileNotFoundError:
        return None
    except OSError as e:
        st.error(f"Error: An OS error occurred - {e}")
        return None
    except Exception as e:
        st.error(f"Error: An unexpected error occurred - {e}")
        return None

def download_and_check_modification_date(csv_path_index):
    kaggle_download.download_dataset()
    return get_file_modification_date(csv_path_index)

def read_files(csvIndex, csvStocks, csvCompanies):
   
   df_index = pd.read_csv(csvIndex)
   df_stocks = pd.read_csv(csvStocks)
   df_companies = pd.read_csv(csvCompanies)

   return df_index, df_stocks, df_companies

def get_yesterday_date():
   yesterday_date = datetime.today() - timedelta(days = 1)
   return yesterday_date

def prepare_sp_line_chart(df):
    df_spIndex = df.copy()
    return df_spIndex

def get_previous_closing_value(df):
   yesterday_date = get_yesterday_date()
   yesterday_date_string = date_to_string(yesterday_date)
   previous_closing_value_row = df.loc[df['Date'] == yesterday_date_string]

   if not previous_closing_value_row.empty:
       return previous_closing_value_row['S&P500'].values[0]
   else:
       return None

def date_to_string(date):
   formatted_date = date.strftime('%Y-%m-%d')
   return str(formatted_date)
