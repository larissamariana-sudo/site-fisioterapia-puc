%%writefile app.py
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Fisioterapia | PUC Goiás",
    page_icon="🩺",
    layout="wide"
)

# --- CABEÇALHO / TEMA INSTITUCIONAL ---
st.markdown("""
    <div style='background-color: #004225; padding: 20px; border-radius: 10px; text-align: center; color: white;'>
        <h1 style='margin:0; font-size: 28px;'>Fisioterapia PUC Goiás</h1>
        <p style='margin:5px 0 0 0; font-size: 16px;'>Portal de Eventos, Anais e Chamadas Acadêmicas</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# --- MENU LATERAL ---
st.sidebar.title("Navegação")
menu = st.sidebar.selectbox("Escolha a seção:", ["Início", "Próximos Eventos (Chamadas)", "Anais de Eventos", "Submissão de Trabalhos"])

# --- SEÇÃO: INÍCIO ---
if menu == "Início":
    st.subheader("Bem-vindo ao Portal Acadêmico de Fisioterapia")
    st.write("""
        Este espaço é dedicado à divulgação científica, chamadas para submissão de trabalhos e publicação de 
        anais dos eventos promovidos pelo curso de Fisioterapia da Pontifícia Universidade Católica de Goiás (PUC Goiás).
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**📅 Próximo Evento em Destaque**\n\nIX Jornada Científica de Fisioterapia da PUC Goiás\nData: Outubro de 2026")
    with col2:
        st.success("**📢 Editais Abertos**\n\nChamada aberta para submissão de resumos científicos até 30/09/2026.")

# --- SEÇÃO: CHAMADAS DE EVENTOS ---
elif menu == "Próximos Eventos (Chamadas)":
    st.subheader("📢 Chamadas Abertas e Editais")
    
    st.markdown("### IX Jornada Científica de Fisioterapia")
    st.write("**Período de Submissão:** 01/09/2026 a 30/09/2026")
    st.write("O comitê organizador convita estudantes, professores e profissionais a submeterem seus resumos científicos nas áreas de Fisioterapia Cardiorrespiratória, Ortopédica, Neurológica e Saúde Coletiva.")
    
    # Botão simulando download de edital
    st.download_button(
        label="📥 Baixar Edital Completo (PDF)",
        data="Conteúdo fictício do edital...",
        file_name="edital_jornada_fisioterapia_pucgo.pdf",
        mime="application/text"
    )

# --- SEÇÃO: ANAIS DE EVENTOS ---
elif menu == "Anais de Eventos":
    st.subheader("📚 Anais de Eventos Publicados")
    st.write("Consulte os cadernos de resumos e anais de edições anteriores dos nossos eventos.")
    
    # Exemplo de Edição Anual
    st.markdown("---")
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.write("**VIII Jornada Científica de Fisioterapia da PUC Goiás (2025)**")
        st.caption("ISSN: 0000-0000 | Publicado em: Dezembro de 2025")
    with col_b:
        st.button("📄 Acessar Anais", key="anais_2025")

    col_c, col_d = st.columns([3, 1])
    with col_c:
        st.write("**VII Jornada Científica de Fisioterapia da PUC Goiás (2024)**")
        st.caption("ISSN: 0000-0000 | Publicado em: Dezembro de 2024")
    with col_d:
        st.button("📄 Acessar Anais", key="anais_2024")

# --- SEÇÃO: SUBMISSÃO ---
elif menu == "Submissão de Trabalhos":
    st.subheader("✍️ Área do Autor / Submissão")
    st.write("Preencha o formulário abaixo para enviar o seu resumo para avaliação.")
    
    with st.form("form_submissao"):
        titulo = st.text_input("Título do Trabalho")
        autor = st.text_input("Nome do Autor Principal")
        email = st.text_input("E-mail para Contato")
        eixo = st.selectbox("Eixo Temático", ["Fisioterapia Ortopédica e Traumatológica", "Fisioterapia Neurológica", "Fisioterapia em Terapia Intensiva", "Saúde da Mulher / Coletiva"])
        arquivo = st.file_uploader("Envie o arquivo do resumo (PDF ou DOCX)", type=["pdf", "docx"])
        
        submitted = st.form_submit_button("Enviar Trabalho")
        if submitted:
            if titulo and autor and arquivo:
                st.success("Trabalho enviado com sucesso! Um comprovante foi simulado para o seu e-mail.")
            else:
                st.error("Por favor, preencha todos os campos obrigatórios e envie o arquivo.")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Universidade Católica de Goiás (PUC Goiás) • Curso de Fisioterapia</p>", unsafe_allow_html=True)
