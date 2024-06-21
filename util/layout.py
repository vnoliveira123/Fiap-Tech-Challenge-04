import streamlit as st
from st_pages import show_pages, Page
import locale

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("./main.py", "Tech Challenge: Fase 4", ":computer:", use_relative_hash=True),
            Page(
                "./pages/analise.py",
                "Exploração e Insights",
                ":chart_with_upwards_trend:",
                use_relative_hash=True,
            ),

              Page(
                "./pages/deploy.py",
                "Deploy",
                ":gear:",
                use_relative_hash=True,
            ),

            Page(
                "./pages/conclusao.py",
                "Conclusão",
                ":white_check_mark:",
                use_relative_hash=True,
            ),
            Page(
                "./pages/referencias.py",
                "Referências",
                ":page_facing_up:",
                use_relative_hash=True,
            ),
        ]
    )
    
    with st.sidebar:
        st.subheader("Cientistas de Dados")
        st.text("André Luiz Pedroso (RM353107)") 
        st.text("David Robert de Oliveira (RM352754)")
        st.text("Lucas Rana Rosa Fernandes (RM353105)") 
        st.text("Raphael Gottstein Alves dos Santos (RM353054)")
        st.text("Wellington Porto Brito (RM352977)")
        st.subheader("Turma")
        st.text("3DTAT")   

        st.divider()
        
        st.subheader("Guia de Instalação e Execução do Aplicativo Localmente")

        # Passo 1: Criação e ativação do ambiente virtual
        st.markdown("**1º** Crie e ative um ambiente virtual:")

        # Criação do ambiente virtual
        st.code("python -m venv venv", language="shell")

        # Ativação do ambiente virtual para Linux
        st.markdown("Para Linux, use:")
        st.code("source venv/bin/activate", language="shell")

        # Ativação do ambiente virtual para Windows
        st.markdown("Para Windows, use:")
        st.code("venv\\Scripts\\activate", language="shell")

        # Passo 2: Instalação das dependências
        st.markdown("**2º** Instale as bibliotecas com as versões corretas:")
        st.code("pip install -r requirements.txt", language="shell")

        # Passo 3: Execução do aplicativo
        st.markdown("**3º** Execute o aplicativo:")
        st.code("streamlit run main.py", language="shell")



        
  
