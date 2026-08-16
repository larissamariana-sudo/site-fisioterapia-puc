import streamlit as st

st.set_page_config(
    page_title="Eventos Científicos | PUC Goiás",
    page_icon="🩺",
    layout="wide"
)

# --- ESTILIZAÇÃO DO CABEÇALHO ---
st.markdown("""
    <div style='background-color: #004225; padding: 25px; border-radius: 10px; text-align: center; color: white;'>
        <h1 style='margin:0; font-size: 26px;'>Eventos Científicos na Saúde, Humanidades e Áreas Afins — PUC Goiás</h1>
        <p style='margin:5px 0 0 0; font-size: 15px;'>Portal de Eventos, Submissões, Anais e Certificação DOI</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# --- MENU DE NAVEGAÇÃO ---
menu = st.sidebar.selectbox("Navegue pelo Portal:", [
    "🏠 Início / Sobre", 
    "🎟️ Inscrições (Eventos)", 
    "✍️ Submissão de Trabalhos", 
    "💳 Taxa de DOI Individual", 
    "📚 Anais Publicados"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    st.subheader("Sobre o Portal Acadêmico de Eventos Científicos")
    st.write("Bem-vindo à plataforma de gestão acadêmica e científica para eventos da PUC Goiás.")

# --- 2. INSCRIÇÕES ---
elif menu == "🎟️ Inscrições (Eventos)":
    st.subheader("🎟️ Inscrição em Eventos")
    
    with st.form("form_inscricao"):
        evento_escolhido = st.selectbox("Selecione o Evento:", [
            "Jornada Científica - Fisioterapia (Gratuito - Estudante/Docente PUC Goiás/Banca Examinadora)", 
            "Jornada Científica - Fisioterapia (Pago - Estudante/Docente/Profissional/Externo)", 
            "Minicurso Prático: Massagem Terapêutica (Pago)"
        ])
        
        nome_insc = st.text_input("Nome Completo")
        email_insc = st.text_input("E-mail")
        vinculo = st.selectbox("Vínculo:", ["Estudante - PUC Goiás", "Docente - PUC Goiás", "Banca Examinadora", "Estudante Externo", "Docente Externo", "Profissional"])
        
        btn_inscrever = st.form_submit_button("Confirmar Inscrição")
        
        if btn_inscrever:
            if nome_insc and email_insc:
                # Aqui exibimos as variáveis que você selecionou nos dois campos
                st.success(f"Inscrição realizada com sucesso!\n\n**Evento:** {evento_escolhido}\n**Vínculo selecionado:** {vinculo}")
            else:
                st.error("Preencha os campos.")

# --- 3. SUBMISSÃO ---
elif menu == "✍️ Submissão de Trabalhos":
    st.subheader("✍️ Submissão de Trabalhos")
    with st.form("form_sub"):
        titulo = st.text_input("Título")
        # Correção da vírgula faltante no seu código original
        categoria = st.selectbox("Categoria:", [
            "Fisioterapia Ortopédica e Desportiva",
            "Fisioterapia em Terapia Intensiva",
            "Fisioterapia Neurológica",
            "Saúde da Mulher",
            "Saúde Coletiva e Políticas Públicas",
            "Tecnologias Digitais e IA na Saúde"
        ])
        arquivo = st.file_uploader("Arquivo", type=["doc", "docx"])
        if st.form_submit_button("Enviar"):
            st.success(f"Trabalho '{titulo}' enviado na categoria {categoria}!")

# --- 4. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação de DOI")
    st.info("Valor: R$ 15,00. Chave PIX: larissa.enf@pucgoias.edu.br")
    comprovante = st.file_uploader("Anexe o comprovante", type=["pdf", "png", "jpg"])
    if st.button("Confirmar Solicitação"):
        st.success("Comprovante recebido! Em até 1 semana seu DOI será emitido.")

# --- 5. ANAIS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Anais")
    st.write("Jornada Científica 2025.")
