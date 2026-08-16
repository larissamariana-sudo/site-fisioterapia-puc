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
    st.subheader("Sobre o Portal Acadêmico")
    st.write("Bem-vindo à plataforma de gestão acadêmica e científica para eventos da PUC Goiás.")

# --- 2. INSCRIÇÕES ---
elif menu == "🎟️ Inscrições (Eventos)":
    st.subheader("🎟️ Inscrição na Jornada Científica do Curso de Fisioterapia")
    st.write("Preencha os dados abaixo. O sistema identificará automaticamente se há taxa com base no seu vínculo.")
    
    with st.form("form_inscricao"):
        nome_insc = st.text_input("Nome Completo")
        email_insc = st.text_input("E-mail de Contato")
        
        # Seleção de Vínculo que comanda a regra de pagamento
        vinculo = st.selectbox("Selecione o seu Vínculo:", [
            "Estudante - PUC Goiás (Gratuito)", 
            "Docente - PUC Goiás (Gratuito)", 
            "Banca Examinadora (Gratuito)", 
            "Estudante Externo (Pago - R$ 5,00)", 
            "Docente Externo / Profissional Externo (Pago - R$ 10,00)"
        ])
        
        # Campo opcional ou condicional de comprovação da PUC
        matricula_puc = ""
        comprovante_vinculo = None
        
        if "PUC Goiás" in vinculo:
            matricula_puc = st.text_input("Nº de Matrícula (Estudante) ou Registro SIAPE (Docente):", placeholder="Ex: 202310000 ou 12345")
        
        # Lógica automática de pagamento baseada no vínculo escolhido
        pagamento_necessario = "Pago" in vinculo
        comprovante_pagamento = None
        
        if pagamento_necessario:
            st.warning("⚠️ **Atenção:** Como você selecionou uma categoria externa, este evento possui taxa de inscrição. Realize o PIX para a chave `larissa.enf@pucgoias.edu.br` e anexe o comprovante abaixo.")
            comprovante_pagamento = st.file_uploader("Enviar Comprovante de Pagamento da Inscrição (PDF/Imagem)", type=["pdf", "png", "jpg"])
        
        btn_inscrever = st.form_submit_button("Confirmar Inscrição")
        
        if btn_inscrever:
            if nome_insc and email_insc:
                if pagamento_necessario and not comprovante_pagamento:
                    st.error("Por favor, anexe o comprovante de pagamento da inscrição.")
                else:
                    status_msg = "Inscrição Gratuita confirmada!" if not pagamento_necessario else "Inscrição realizada! Comprovante enviado para validação financeira."
                    st.success(f"Inscrição realizada com sucesso!\n\n- **Nome:** {nome_insc}\n- **Vínculo:** {vinculo}\n- **Status:** {status_msg}")
            else:
                st.error("Preencha os campos obrigatórios (Nome e E-mail).")

# --- 3. SUBMISSÃO ---
elif menu == "✍️ Submissão de Trabalhos":
    st.subheader("✍️ Submissão de Trabalhos Científicos/Resumo Expandido")
    with st.form("form_submissao_trabalho"):
        titulo_trab = st.text_input("Título do Resumo")
        autor_princ = st.text_input("Autor Principal")
        coautores = st.text_area("Coautores (separados por vírgula)")
        
        categoria = st.selectbox("Selecione a Categoria / Eixo Temático:", [
            "Fisioterapia Ortopédica, Reumatológica, Traumatológica e Desportiva",
            "Fisioterapia em Terapia Intensiva e Cardiorrespiratória",
            "Fisioterapia Neurológica e Pediátrica",
            "Saúde da Mulher, Pélvica e Oncológica",
            "Saúde Coletiva, Políticas Públicas e Inovação em Saúde",
            "Tecnologias Digitais e Inteligência Artificial na Saúde"
        ])
        
        arquivo_resumo = st.file_uploader("Arquivo do Resumo (Template padrão Word)", type=["doc", "docx"])
        
        btn_submeter = st.form_submit_button("Enviar Trabalho para Avaliação")
        if btn_submeter:
            if titulo_trab and autor_princ and arquivo_resumo:
                st.success(f"Trabalho submetido com sucesso na categoria **{categoria}**! O código de rastreio foi gerado.")
            else:
                st.error("Preencha todos os campos obrigatórios e anexe o arquivo do resumo.")

# --- 4. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("A publicação nos Anais oficiais com ISBN é gratuita. O DOI individual é opcional.")
    st.info("ℹ️ **Valor:** R$ 15,00. **Chave PIX:** larissa.enf@pucgoias.edu.br")
    
    with st.form("form_doi"):
        id_trabalho = st.text_input("ID ou Título Exato do Trabalho Aprovado")
        autor_resp = st.text_input("Nome do Autor Responsável pelo Pagamento")
        comprovante_doi = st.file_uploader("Anexe o Comprovante do PIX da Taxa de DOI", type=["pdf", "png", "jpg"])
        
        btn_solicitar_doi = st.form_submit_button("Validar e Requisitar DOI")
        if btn_solicitar_doi:
            if id_trabalho and comprovante_doi:
                st.success("Comprovante enviado com sucesso! O DOI será emitido em até 1 semana.")
            else:
                st.error("Informe o título do trabalho e envie o comprovante.")

# --- 5. ANAIS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Repositório de Anais de Fisioterapia")
    st.write("Acesse os cadernos de resumos de edições anteriores.")
    st.markdown("---")
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write("**Jornada Científica do Curso de Fisioterapia da PUC Goiás (2025)**")
        st.caption("ISBN: 0000-0000")
    with col2:
        st.button("📥 Baixar Anais", key="download_2025")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Pontifícia Universidade Católica de Goiás (PUC Goiás) • Saúde e Sociedade FST Fisioterapia</p>", unsafe_allow_html=True)
