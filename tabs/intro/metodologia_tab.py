import streamlit as st
from tabs.tab import TabInterface

class MetodologiaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':gray[Utilização do Power BI e Streamlit para Estrutura de MVP]', divider='orange')
            st.markdown('''
                Para a realização deste trabalho, utilizou-se a ferramenta Power BI para a criação de gráficos interativos, aliada ao Streamlit para o desenvolvimento do MVP (Minimum Viable Product, ou Produto Mínimo Viável) do modelo em produção. Essa combinação permitiu a criação de um dashboard dinâmico e informativo, essencial para fornecer insights sobre o preço do petróleo e suas influências.
            ''')

            st.image('assets/img/streamlit_powerbi.png', caption='MVP: Streamlit + PowerBI')
            