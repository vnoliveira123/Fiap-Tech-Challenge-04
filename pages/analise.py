import streamlit as st
from tabs.analise.modelo_mlearning_tab import LSTMTab
from tabs.analise.metodologia_tab import MetodologiaTab
from tabs.analise.power_bi_insights_tab import PowerBIInsightsTab 
from tabs.analise.resultados_tab import ResultadosTab
from util.layout import output_layout

st.set_page_config(page_title="Análise | Tech Challenge 4 | FIAP", layout='wide')
output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.header(":orange[Exploração e Insights]")

    tab0, tab1, tab2, tab3 = st.tabs(
        tabs=[
            "Long Short-Term Memory Networks (LSTM)",
            "Metodologia",
            "Análises Power BI", 
            "Resultados"
        ]
    )

    LSTMTab(tab0)
    MetodologiaTab(tab1)
    PowerBIInsightsTab(tab2) 
    ResultadosTab(tab3)
     
