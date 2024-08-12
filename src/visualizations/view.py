import streamlit as st
from datetime import datetime
import plotly.graph_objects as go

def configure_line_chart(processed_sp_index):
    fechas = processed_sp_index['Date']
    valores = processed_sp_index['S&P500']

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=fechas,
        y=valores,
        fill='tozeroy',  # Rellena el área debajo de la línea
        mode='lines',
        line=dict(color='green'),
        fillcolor='rgba(0, 255, 0, 0.2)'
    ))

    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='S&P500 Stock',
        template='plotly_white',
        hovermode='x unified',
        modebar=dict(
          bgcolor='rgba(0,0,0,0)',
          color='rgba(0,0,0,0)',
          remove=['zoom', 'pan', 'select', 'zoomIn', 'zoomOut', 'resetScale', 'toggleSpikelines']
        )
    )
    return fig

def create_sp_index_line_chart(chart_placeholder, processed_sp_index, previous_closing_value):
        chart = configure_line_chart(processed_sp_index)
        with chart_placeholder.container(border=True):
            st.header('Evolución del S&P500')
            st.write(datetime.now().strftime("%d-%m-%Y"))
            st.markdown(f"Cierre anterior ({previous_closing_value['Date'].values[0]}): {previous_closing_value['S&P500'].values[0]}")
            st.plotly_chart(chart)
            st.markdown(long_text)

def side_bar():
      with st.sidebar:
        return st.selectbox('Elige un periodo', ("Histórico","5 Días", "1 Mes", "6 Meses", "1 Año") )

long_text = "El índice Standard & Poor's 500, también conocido como S&P 500, es uno de los índices bursátiles más importantes de Estados Unidos. Al S&P 500 se le considera el índice más representativo de la situación real del mercado.​El índice se basa en la capitalización bursátil de 500 grandes empresas que poseen acciones que cotizan en las bolsas NYSE o NASDAQ, y captura aproximadamente el 80% de toda la capitalización de mercado en Estados Unidos. Los componentes del índice S&P 500 y su ponderación son determinados por S&P Dow Jones Indices. Se diferencia de otros índices de mercados financieros de Estados Unidos, tales como el Dow Jones Industrial Average o el índice Nasdaq Composite, en la diversidad de los rubros que lo conforman y en su metodología de ponderación. Es uno de los índices de valores más seguidos, y muchas personas lo consideran el más representativo del mercado de acciones de Estados Unidos, y el marcador de tendencias de la economía norteamericana.​"
