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
    mostrar_cabecalho("PORTAL.jpg")
    st.subheader("🎟️ Programação de Eventos e Cursos Disponíveis")
    st.write("Selecione abaixo o evento de seu interesse para ver os detalhes e realizar a inscrição.")
    
    evento_selecionado = st.selectbox("Escolha o Evento:", [
        "1. Jornada Científica do Curso de Fisioterapia", 
        "2. Minicurso Prático: Reabilitação e Terapia Manual", 
        "3. Workshop: Inovação e Tecnologias em Saúde",
        "4. Simpósio de Saúde Coletiva e Políticas Públicas"
    ])
    
    st.markdown("---")
    
    if "Jornada Científica" in evento_selecionado:
        st.image("logo_jornada.png.jpg", use_container_width=True)
        st.markdown("### 🩺 Jornada Científica do Curso de Fisioterapia")
        st.write("""
        * **Público-alvo:** Estudantes, docentes, profissionais e pesquisadores.
        * **Investimento:** 
          * Estudantes, Docentes e Banca da PUC Goiás: **Gratuito**.
          * Participantes Externos: **R$ 10,00** (Standby mediante comprovante na chave `eventoscientificosc@gmail.com`).
        * **Destaque:** Permite submissão de Resumos Simples, Expandidos e Artigos Completos com ISBN gratuito.
        """)
        st.markdown("### **EIXOS TEMÁTICOS**")
        st.write("**Fisioterapia Musculo Esquelética, Neurológica, Cardiorrespiratória, Terapia Intensiva, Geriatria e Gerontologia, Saúde da Mulher, Saúde Coletiva, Tecnologias e Inteligência Artificial na Saúde e Outras Áreas.**")
        st.warning("⚠️ **Atenção para inscrições pagas:** Ficarão em status de **Standby** até a validação do comprovante.")
    
    # Categorias de Inscrição e Cadastro de Trabalhos
    cat = st.radio("Selecione a opção desejada:", [
        "Participante/Ouvinte", 
        "Apresentador de Trabalho", 
        "Membro da Banca", 
        "Cadastro de Trabalho para Certificação (Orientador)"
    ])
    
    if cat == "Participante/Ouvinte":
        st.link_button("🔗 Inscrever-se como Ouvinte", "https://forms.gle/pimCxShsFgc9tg5d9")
    elif cat == "Apresentador de Trabalho":
        st.link_button("🔗 Inscrever-se como Apresentador", "https://forms.gle/mgLc9iaibDfBYqi78")
    elif cat == "Membro da Banca":
        st.link_button("🔗 Inscrever-se como Banca", "https://forms.gle/mgLc9iaibDfBYqi78")
    else:
        st.info("⚠️ **Exclusivo para Orientadores:** Utilize este formulário para cadastrar o título do trabalho, nome completo do estudante e dos membros da banca examinadora, para elaboração do certificado.")
        st.link_button("📝 Cadastrar Informações do Trabalho", "https://forms.gle/bTGR48dU3rrgBgr17")

# --- 3. TRABALHOS (SUBMISSÃO + STATUS) ---
elif menu == "✍️ Trabalhos Científicos":
    st.subheader("✍️ Central de Trabalhos Científicos")
    tab1, tab2 = st.tabs(["📥 Submissão", "🔍 Consultar Status"])
    with tab1:
        st.write("Consulte as normas e utilize o link do formulário para enviar seu arquivo Word.")
        st.link_button("📥 Acessar Formulário de Submissão", "https://forms.gle/sRzBuCbMzatAcUZH7")
    with tab2:
        st.write("Digite o e-mail cadastrado para verificar o parecer da comissão.")
        email = st.text_input("E-mail cadastrado:")
        if st.button("Consultar Status"):
            st.info("https://docs.google.com/spreadsheets/d/1X7XoT0ohgtc5DZOw-ezcu0HjPPSaBF-nSrGWOFSVsUY/edit?usp=sharing")

# --- 4. CERTIFICADOS (EMISSÃO + VALIDAÇÃO) ---
elif menu == "🎓 Certificados e Validação":
    st.subheader("🎓 Certificados")
    tab1, tab2 = st.tabs(["📜 Emitir Certificado", "🛡️ Validar Autenticidade"])
    with tab1:
        cat_cert = st.selectbox("Categoria:", ["Ouvinte (16h)", "Apresentador (5h)", "Banca Avaliadora"])
        st.link_button("📥 Emitir Certificado", "COLE_LINK_EMISSAO_AQUI")
    with tab2:
        codigo = st.text_input("Digite o código de autenticidade (ex: PUCGO-2026-XXXX):")
        if st.button("Validar"):
            st.info("Insira o link da planilha de certificados para habilitar a validação.")

# --- 5. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("A publicação nos Anais oficiais com ISBN é gratuita. O DOI individual é opcional (R$ 15,00).")
    st.info("ℹ️ **Chave PIX:** eventoscientificosc@gmail.com")
    st.link_button("🔗 Link para Solicitação DOI", "COLE_LINK_DOI_AQUI")

# --- 6. ANAIS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Repositório Oficial de Anais")
    st.write("Acesse abaixo os cadernos de resumos e anais oficiais.")
    st.link_button("📥 Baixar Anais", "COLE_LINK_PDF_ANAIS_AQUI")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Tecnologias • Saúde e Sociedade FST Fisioterapia | PUC Goiás</p>", unsafe_allow_html=True)
