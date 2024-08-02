import pandas as pd

def read_files(csvIndex, csvStocks, csvCompanies):
   
   df_index = pd.read_csv(csvIndex)
   df_stocks = pd.read_csv(csvStocks)
   df_companies = pd.read_csv(csvCompanies)

   return df_index, df_stocks, df_companies

def prepare_sp_line_chart(df):
    df_spIndex = df.copy()
    return df_spIndex