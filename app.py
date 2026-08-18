import streamlit as st

st.set_page_config(
    page_title="Eventos Científicos | PUC Goiás",
    page_icon="🩺",
    layout="wide"
)

# --- FUNÇÕES DE ESTILO ---
def mostrar_cabecalho(foto="logo_jornada.png.jpg"):
    st.image(foto, use_container_width=True)
    st.markdown("""
        <div style='background-color: #004225; padding: 25px; border-radius: 10px; text-align: center; color: white;'>
            <h1 style='margin:0; font-size: 26px;'>Eventos Científicos na Saúde, Humanidades e Áreas Afins — PUC Goiás</h1>
        </div>
    """, unsafe_allow_html=True)
    st.write("")

# --- MENU ---
menu = st.sidebar.selectbox("Navegue pelo Portal:", [
    "🏠 Início / Sobre", 
    "🎟️ Eventos e Inscrições", 
    "✍️ Trabalhos Científicos", 
    "🎓 Certificados e Validação", 
    "💳 Taxa de DOI Individual", 
    "📚 Anais Publicados"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    mostrar_cabecalho("PORTAL.jpg")
    st.subheader("Bem-vindo ao Portal de Eventos Científicos da FST da PUC Goiás")
    st.write("Central oficial de gestão acadêmica e científica.")

# --- 2. EVENTOS E INSCRIÇÕES ---
elif menu == "🎟️ Eventos e Inscrições":
    mostrar_cabecalho("logo_jornada.png.jpg")
    st.subheader("🎟️ Programação de Eventos")
    
    evento = st.selectbox("Escolha o Evento:", [
        "Jornada Científica (Fisioterapia)", 
        "Minicurso Prático: Terapia Manual", 
        "Workshop: Inovação em Saúde",
        "Simpósio de Saúde Coletiva"
    ])
    
    st.markdown("---")
    # Categorias de inscrição
    cat = st.radio("Selecione sua categoria:", ["Participante/Ouvinte", "Apresentador de Trabalho", "Membro da Banca"])
    
    if cat == "Participante/Ouvinte":
        st.link_button("🔗 Inscrever-se como Ouvinte", "LINK_OUVINTE")
    elif cat == "Apresentador de Trabalho":
        st.link_button("🔗 Inscrever-se como Apresentador", "LINK_APRESENTADOR")
    else:
        st.link_button("🔗 Inscrever-se como Banca", "LINK_BANCA")

# --- 3. TRABALHOS (SUBMISSÃO + STATUS) ---
elif menu == "✍️ Trabalhos Científicos":
    st.subheader("✍️ Central de Trabalhos Científicos")
    tab1, tab2 = st.tabs(["📥 Submissão", "🔍 Consultar Status"])
    
    with tab1:
        st.write("Envie seu arquivo Word (.doc/.docx) via formulário.")
        st.link_button("📥 Acessar Formulário de Submissão", "LINK_SUBMISSAO")
        
    with tab2:
        st.write("Consulte o parecer da comissão científica.")
        email = st.text_input("E-mail cadastrado:")
        if st.button("Consultar"):
            st.warning("Insira o link da planilha aqui para habilitar a consulta.")

# --- 4. CERTIFICADOS (EMISSÃO + VALIDAÇÃO) ---
elif menu == "🎓 Certificados e Validação":
    st.subheader("🎓 Certificados")
    tab1, tab2 = st.tabs(["📜 Emitir Certificado", "🛡️ Validar Autenticidade"])
    
    with tab1:
        st.write("Selecione a categoria para receber seu certificado:")
        cat_cert = st.selectbox("Categoria:", ["Ouvinte (20h)", "Apresentador (5h)", "Banca Avaliadora"])
        st.link_button("📥 Emitir Certificado", "LINK_CERTIFICADOS")
        
    with tab2:
        st.write("Digite o código de autenticidade (ex: PUCGO-2026-XXXX):")
        codigo = st.text_input("Código:")
        if st.button("Validar"):
            st.info("Insira o link da planilha para habilitar a validação.")

# --- 5. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação de DOI")
    st.link_button("🔗 Solicitar DOI", "LINK_DOI")

# --- 6. ANAIS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Repositório de Anais")
    st.link_button("📥 Baixar Anais", "LINK_ANAIS")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Tecnologias • Saúde e Sociedade FST Fisioterapia | PUC Goiás</p>", unsafe_allow_html=True)
