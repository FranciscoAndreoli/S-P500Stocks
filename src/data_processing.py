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

def download_and_check_modification_date(csv_path_stocks):
    kaggle_download.download_dataset()
    return get_file_modification_date(csv_path_stocks)

def read_index_file(csvIndex):
   df_index = pd.read_csv(csvIndex)

   return df_index

def read_stock_file(csvStocks):
   df_stocks = pd.read_csv(csvStocks)

   return df_stocks

def read_companies_file(csvCompanies):
   df_companies = pd.read_csv(csvCompanies)

   return df_companies

def prepare_sp_line_chart(df):
    df_spIndex = df.copy()
    
    return df_spIndex

def prepare_filtered_sp_line_chart(df, period):
    df_spIndex = df.tail(period)

    return df_spIndex


def get_previous_date(numDays):
   past_date = datetime.today() - timedelta(days = numDays)
   return past_date

def get_previous_closing_value(df, value):
    past_date = get_previous_date(value)
    past_date_string = date_to_string(past_date)
    previous_closing_value_row = df.loc[df['Date'] == past_date_string]

    if not previous_closing_value_row.empty:
        return previous_closing_value_row #['S&P500'].values[0]
    else:
        return df.tail(1)

def date_to_string(date):
   formatted_date = date.strftime('%Y-%m-%d')
   return str(formatted_date)
