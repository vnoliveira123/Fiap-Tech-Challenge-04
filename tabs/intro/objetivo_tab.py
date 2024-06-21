import streamlit as st
from tabs.tab import TabInterface

class ObjetivoTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':gray[Desvendando o Mercado do Petróleo: Dashboard Interativo com Storytelling e ML]', divider='orange')
            st.markdown('''
                 O objetivo do desafio é desenvolver um dashboard interativo que integre storytelling com um modelo de machine learning para prever o preço diário do petróleo. O dashboard busca ser informativo, envolvente e acessível, fornecendo insights significativos sobre as variações do preço do petróleo, derivados de fatores como geopolítica, crises econômicas, demanda global por energia e avanços tecnológicos.
            ''')

            st.image('assets/img/refinaria.png', caption='Refinaria de petróleo: transformando o ouro negro em produtos essenciais')