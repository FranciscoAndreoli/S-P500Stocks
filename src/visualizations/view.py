import streamlit as st
def create_sp_index_line_chart(processed_sp_index, previous_closing_value):
        with st.container(border=True):
            st.write(previous_closing_value)
            st.line_chart(processed_sp_index, x="Date", y="S&P500", x_label=None, y_label="S&P500 Stock")

def initialize_sideBar():
      with st.sidebar:
        st.radio("Filtros", ("Por mes", "Por año") )
