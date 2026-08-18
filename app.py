import streamlit as st

st.set_page_config(
    page_title="Eventos Científicos | PUC Goiás",
    page_icon="🩺",
    layout="wide"
)

# --- FUNÇÃO DE CABEÇALHO CONDICIONAL ---
def mostrar_cabecalho():
    st.image("logo_jornada.png.jpg", use_container_width=True)
    st.markdown("""
        <div style='background-color: #004225; padding: 25px; border-radius: 10px; text-align: center; color: white;'>
            <h1 style='margin:0; font-size: 26px;'>Eventos Científicos na Saúde, Humanidades e Áreas Afins — PUC Goiás</h1>
            <p style='margin:5px 0 0 0; font-size: 15px;'>Portal de Eventos, Submissões, Anais e Certificação DOI</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("")

# --- MENU ---
menu = st.sidebar.selectbox("Navegue pelo Portal:", [
    "🏠 Início / Sobre", 
    "🎟️ Eventos e Inscrições", 
    "✍️ Submissão de Trabalhos", 
    "🔍 Consultar Status do Trabalho", 
    "🎓 Certificados e Validação", 
    "💳 Taxa de DOI Individual", 
    "📚 Anais Publicados"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    mostrar_cabecalho()
    st.subheader("Bem-vindo ao Portal de Eventos Científicos da FST da PUC Goiás")
    st.write("Central oficial de gestão acadêmica e certificação.")

# --- 2. EVENTOS E INSCRIÇÕES ---
elif menu == "🎟️ Eventos e Inscrições":
    mostrar_cabecalho()
    st.subheader("🎟️ Selecione sua Categoria de Inscrição")
    
    categoria = st.selectbox("Quem é você no evento?", [
        "Selecione...",
        "Participante / Ouvinte",
        "Apresentador de Trabalho",
        "Membro da Banca Avaliadora"
    ])
    
    if categoria == "Participante / Ouvinte":
        st.info("Inscrições para ouvintes que desejam receber certificado de 20h.")
        st.link_button("🔗 Inscrever-se como Ouvinte", "COLE_AQUI_O_LINK_DO_FORMULARIO_OUVINTE")
        
    elif categoria == "Apresentador de Trabalho":
        st.info("Inscrições para autores/apresentadores que receberão certificado de 5h.")
        st.link_button("🔗 Inscrever-se como Apresentador", "COLE_AQUI_O_LINK_DO_FORMULARIO_APRESENTADOR")
        
    elif categoria == "Membro da Banca Avaliadora":
        st.info("Inscrições para membros da banca avaliadora com emissão de certificado nominal.")
        st.link_button("🔗 Inscrever-se como Banca", "COLE_AQUI_O_LINK_DO_FORMULARIO_BANCA")

# --- 3. SUBMISSÃO ---
elif menu == "✍️ Submissão de Trabalhos":
    st.subheader("✍️ Central de Submissão")
    st.write("Utilize o link abaixo para enviar seu trabalho (Formulário no Drive de alta capacidade).")
    st.link_button("📥 Enviar Trabalho", "COLE_AQUI_O_LINK_DO_FORMULARIO_SUBMISSAO")

# --- 4. STATUS ---
elif menu == "🔍 Consultar Status do Trabalho":
    st.subheader("🔍 Consultar Status")
    with st.form("form_status"):
        email = st.text_input("E-mail cadastrado:")
        if st.form_submit_button("Consultar"):
            # Substitua o link abaixo pela sua nova planilha do Drive
            st.warning("Configuração de planilha pendente: Insira o link da sua nova planilha no código.")

# --- 5. CERTIFICADOS ---
elif menu == "🎓 Certificados e Validação":
    st.subheader("🎓 Validação de Certificados")
    codigo = st.text_input("Digite o código de autenticidade impresso no rodapé:")
    if st.button("Validar"):
        st.info("Aguardando configuração de banco de dados no Drive.")

# --- 6. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação de DOI")
    st.info("Pagamento via PIX: eventoscientificospucgoias@hotmail.com")
    st.link_button("🔗 Link para Solicitação DOI", "COLE_AQUI_O_LINK_DO_FORMULARIO_DOI")

# --- 7. ANAIS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Repositório de Anais")
    st.link_button("📥 Baixar Anais Oficiais", "COLE_AQUI_O_LINK_DO_PDF_FINAL_NO_DRIVE")

# --- RODAPÉ (Aparece em todas) ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Tecnologias • Saúde e Sociedade FST Fisioterapia | PUC Goiás</p>", unsafe_allow_html=True)
