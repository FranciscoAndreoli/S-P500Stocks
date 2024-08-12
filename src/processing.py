import data_processing
from visualizations import view

def process_and_visualize_data(chart_placeholder, df_index):
    processed_sp_index = data_processing.prepare_sp_line_chart(df_index)
    previous_closing_value = data_processing.get_previous_closing_value(df_index, 1)
    view.create_sp_index_line_chart(chart_placeholder, processed_sp_index, previous_closing_value)

def process_and_visualize_filtered_data(chart_placeholder, df_index, period):
    processed_sp_index = data_processing.prepare_filtered_sp_line_chart(df_index, period)
    previous_closing_value = data_processing.get_previous_closing_value(df_index, period)
    view.create_sp_index_line_chart(chart_placeholder, processed_sp_index, previous_closing_value)