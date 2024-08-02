import streamlit as st
def create_sp_index_line_chart(processed_sp_index):
        with st.container(height=500, border=True):
            st.write("This is inside the container")
            st.line_chart(processed_sp_index,x="Date",y="S&P500",x_label=None,y_label="S&P500 Stock")

def initialize_sideBar():
      with st.sidebar:
        st.radio("Filtros", ("Por mes", "Por año") )
