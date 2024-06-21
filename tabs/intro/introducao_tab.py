import streamlit as st
from tabs.tab import TabInterface

class IntroTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':gray[Navegando pelas Oscilações do Mercado do Petróleo]', divider='orange')
            st.markdown('''
            O mercado global de petróleo é um cenário de constante turbulência, onde cada variação no preço do barril pode ter impactos significativos em diversas esferas da economia mundial. Nesse contexto, compreender os insights que moldam essas oscilações torna-se crucial para empresas, investidores e governos, permitindo-lhes antecipar mudanças, mitigar riscos e identificar oportunidades estratégicas.\n
            O presente artigo apresenta quatro insights fundamentais que delineiam a variação do preço do petróleo, desde fatores geopolíticos até avanços tecnológicos. Ao explorar esses insights, mergulharemos em um universo complexo e interconectado, onde geopolítica, crises econômicas, demanda energética e inovações tecnológicas convergem para moldar o panorama do mercado do petróleo.\n
            A análise detalhada desses insights não apenas oferece uma compreensão mais profunda das forças que impulsionam as flutuações do preço do petróleo, mas também fornece um guia para tomar decisões estratégicas informadas. Ao longo deste artigo, examinaremos cada insight com exemplos concretos e destacaremos sua relevância no contexto do mercado global de energia.\n
            Portanto, prepare-se para uma jornada pela geopolítica, crises econômicas, demanda energética e inovações tecnológicas, enquanto desvendamos os mistérios por trás das oscilações do preço do petróleo e exploramos as implicações desses insights para o futuro do mercado energético global.
            ''')
           
            st.image('assets/img/oil-and-gas.jpg', caption='Extração de petróleo: alimentando o mundo com energia', use_column_width=True, output_format='auto')
