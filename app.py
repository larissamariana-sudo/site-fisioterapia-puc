import streamlit as st

st.set_page_config(
    page_title="Eventos Científicos | Saúde, Humanidades e Áreas Afins",
    page_icon="🩺",
    layout="wide"
)

# --- FUNÇÕES DE ESTILO ---
def mostrar_cabecalho(foto="PORTAL.jpg"):
    st.image(foto, use_container_width=True)
    st.markdown("""
        <div style='background-color: #004225; padding: 25px; border-radius: 10px; text-align: center; color: white;'>
            <h1 style='margin:0; font-size: 26px;'>Eventos Científicos na Saúde, Humanidades e Áreas Afins</h1>
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
    st.subheader("Bem-vindo ao Portal de Eventos Científicos na Saúde, Humanidades e Áreas Afins")
   st.write("Central oficial de gestão acadêmica, submissão de resumos, acompanhamento de avaliação e publicação de anais.")
    st.markdown("""
    
    * **Inscrições:** Gratuitas para PUC Goiás / Pagas (Standby) para externos mediante envio de comprovante.
    * **Submissões:** Realizadas via formulário específico com normas detalhadas por modalidade.
    * **Avaliação:** Acompanhe em tempo real se seu trabalho está em análise, aprovado ou pendente de correções.
    """)

# --- 2. EVENTOS E INSCRIÇÕES ---
elif menu == "🎟️ Eventos e Inscrições":
    mostrar_cabecalho("logo_jornada.png.jpg")
   st.subheader("🎟️ Programação de Eventos e Cursos Disponíveis")
    st.write("Selecione abaixo o evento de seu interesse para ver os detalhes, normas e realizar a inscrição.")
    
    evento_selecionado = st.selectbox("Escolha o Evento:", [
        "1. Jornada Científica do Curso de Fisioterapia", 
        "2. Minicurso Prático: Reabilitação e Terapia Manual", 
        "3. Workshop: Inovação e Tecnologias em Saúde",
        "4. Simpósio de Saúde Coletiva e Políticas Públicas"
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
