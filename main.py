import streamlit as st
from tabs.intro.introducao_tab import IntroTab
from tabs.intro.metodologia_tab import MetodologiaTab
from tabs.intro.objetivo_tab import ObjetivoTab 
from util.layout import output_layout
import warnings

warnings.filterwarnings("ignore")

output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.header(':orange[FIAP PÓS TECH – DATA ANALYTICS, 2024]')

    tab0, tab1, tab2 = st.tabs(tabs=['Introdução', 'Objetivo', 'Metodologia'])

    IntroTab(tab0)
    ObjetivoTab(tab1)
    MetodologiaTab(tab2)