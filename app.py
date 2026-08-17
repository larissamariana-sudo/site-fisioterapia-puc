import streamlit as st

st.set_page_config(
    page_title="Fisioterapia | PUC Goiás",
    page_icon="🩺",
    layout="wide"
)

# --- ESTILIZAÇÃO DO CABEÇALHO INSTITUCIONAL ---
st.markdown("""
    <div style='background-color: #004225; padding: 25px; border-radius: 10px; text-align: center; color: white;'>
        <h1 style='margin:0; font-size: 26px;'>Curso de Fisioterapia — PUC Goiás</h1>
        <p style='margin:5px 0 0 0; font-size: 15px;'>Portal Oficial de Eventos, Submissões, Anais e Certificação DOI</p>
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

# --- 1. INÍCIO / DESCRIÇÃO ---
if menu == "🏠 Início / Sobre":
    st.subheader("Sobre o Portal Acadêmico")
    st.write("""
        Bem-vindo à plataforma oficial de gestão acadêmica e científica do curso de Fisioterapia da 
        **Pontifícia Universidade Católica de Goiás (PUC Goiás)**. Este portal centraliza:
    """)
    st.markdown("""
    - **Inscrições** em jornadas, simpósios e cursos de extensão;
    - **Submissão de resumos científicos** divididos por eixos temáticos;
    - **Publicação de Anais** oficiais com rastreabilidade acadêmica;
    - **Solicitação opcional de DOI individual** para artigos aprovados.
    """)
    st.info("💡 **Destaque Atual:** As inscrições e submissões para o ECIF (Encontro Científico de Fisioterapia) já estão abertas!")

# --- 2. INSCRIÇÕES PARA EVENTOS ---
elif menu == "🎟️ Inscrições (Eventos)":
    st.subheader("🎟️ Inscrição em Eventos e Cursos")
    st.write("Faça sua inscrição para as palestras, mesas-redondas e minicursos.")
    
    with st.form("form_inscricao"):
        evento_escolhido = st.selectbox("Selecione o Evento:", [
            "IX Encontro Científico de Fisioterapia (Gratuito - Apenas Ouvinte)", 
            "Minicurso Prático: Reabilitação Vestibular (Pago - R$ 30,00)", 
            "Workshop de Termografia Clínica (Pago - R$ 50,00)"
        ])
        
        nome_insc = st.text_input("Nome Completo")
        email_insc = st.text_input("E-mail Institucional ou de Contato")
        vinculo = st.selectbox("Vínculo com a Instituição", ["Estudante Fisioterapia - PUC Goiás", "Estudante Externo", "Profissional / Fisioterapeuta"])
        
        # Lógica visual condicional se for evento pago
        if "Pago" in evento_escolhido:
            st.warning("⚠️ Este evento possui taxa de inscrição. Após enviar os dados, você receberá a chave PIX/boleto no e-mail informado para envio do comprovante.")
            comprovante_pagamento = st.file_uploader("Enviar Comprovante de Inscrição (PDF/Imagem)", type=["pdf", "png", "jpg"])
        
        btn_inscrever = st.form_submit_button("Confirmar Inscrição")
        if btn_inscrever:
            if nome_insc and email_insc:
                st.success(f"Inscrição realizada com sucesso para: **{evento_escolhido}**! Um e-mail de confirmação foi disparado.")
            else:
                st.error("Preencha todos os campos obrigatórios.")

# --- 3. SUBMISSÃO DE RESUMOS EM DIFERENTES CATEGORIAS ---
elif menu == "✍️ Submissão de Resumos de Trabalhos":
    st.subheader("✍️ Submissão de Trabalhos Científicos")
    st.write("Envie o seu resumo para avaliação da comissão científica do evento.")
    
    with st.form("form_submissao_trabalho"):
        titulo_trab = st.text_input("Título do Resumo")
        autor_princ = st.text_input("Autor Principal")
        coautores = st.text_area("Coautores (separados por vírgula)")
        
        categoria = st.selectbox("Selecione a Categoria / Eixo Temático:", [
            "Fisioterapia Ortopédica, Traumatológica e Desportiva",
            "Fisioterapia em Terapia Intensiva e Cardiorrespiratória",
            "Fisioterapia Neurológica e Pediátrica",
            "Saúde da Mulher, Pélvica e Oncológica",
            "Saúde Coletiva, Políticas Públicas e Inovação em Saúde"
        ])
        
        arquivo_resumo = st.file_uploader("Arquivo do Resumo (Template padrão Word/PDF)", type=["doc", "docx", "pdf"])
        
        btn_submeter = st.form_submit_button("Enviar Trabalho para Avaliação")
        if btn_submeter:
            if titulo_trab and autor_princ and arquivo_resumo:
                st.success(f"Trabalho submetido com sucesso na categoria **{categoria}**! O código de rastreio foi gerado.")
            else:
                st.error("Preencha todos os campos obrigatórios e anexe o arquivo do resumo.")

# --- 4. PAGAMENTO DE DOI INDIVIDUAL ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("""
        A publicação nos Anais oficiais do evento é **totalmente gratuita**. No entanto, caso você deseje 
        um **DOI (Digital Object Identifier) individual e exclusivo** para o seu artigo publicado (ideal para Lattes e Pós-Graduação), 
        é cobrada uma taxa de emissão de registro internacional.
    """)
    
    st.info("ℹ️ **Valor da Taxa de DOI Individual:** R$ 25,00 por trabalho aceito.")
    
    with st.form("form_doi"):
        id_trabalho = st.text_input("ID ou Título Exato do Trabalho Aprovado")
        autor_resp = st.text_input("Nome do Autor Responsável pelo Pagamento")
        
        # Simulação de integração de pagamento via PIX (Geração de QR Code / Chave Copia e Cola)
        st.markdown("### Dados para Pagamento via PIX:")
        st.code("Chave PIX (CNPJ/E-mail da fundação/suporte): 00.000.000/0001-00 (Exemplo PUC Goiás/Eventos)")
        
        comprovante_doi = st.file_uploader("Anexe o Comprovante do PIX da Taxa de DOI", type=["pdf", "png", "jpg"])
        
        btn_solicitar_doi = st.form_submit_button("Validar e Requisitar DOI")
        if btn_solicitar_doi:
            if id_trabalho and comprovante_doi:
                st.success("Comprovante enviado com sucesso! Nosso setor financeiro validará o pagamento e o DOI será emitido em até 48 horas.")
            else:
                st.error("Por favor, informe o título do trabalho e envie o comprovante de pagamento.")

# --- 5. ANAIS DE EVENTOS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Repositório de Anais de Fisioterapia")
    st.write("Acesse os cadernos de resumos de edições anteriores.")
    st.markdown("---")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write("**XX Encontro Científico de Fisioterapia da PUC Goiás (2025)**")
        st.caption("ISSN: 2358-0000 | Artigos com e sem DOI individual.")
    with col2:
        st.button("📥 Baixar Anais", key="download_2025")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Pontifícia Universidade Católica de Goiás (PUC Goiás) • Departamento de Fisioterapia</p>", unsafe_allow_html=True)
