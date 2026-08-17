import streamlit as st

st.set_page_config(
    page_title="Eventos Científicos | PUC Goiás",
    page_icon="🩺",
    layout="wide"
)

# --- ESTILIZAÇÃO DO CABEÇALHO ---
st.image("logo_jornada.png.jpg", use_container_width=True)
st.markdown("""
    <div style='background-color: #004225; padding: 25px; border-radius: 10px; text-align: center; color: white;'>
        <h1 style='margin:0; font-size: 26px;'>Eventos Científicos na Saúde, Humanidades e Áreas Afins — PUC Goiás</h1>
        <p style='margin:5px 0 0 0; font-size: 15px;'>Portal de Eventos, Submissões, Anais e Certificação DOI</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# --- MENU DE NAVEGAÇÃO PRINCIPAL ---
menu = st.sidebar.selectbox("Navegue pelo Portal:", [
    "🏠 Início / Sobre", 
    "🎟️ Eventos e Inscrições", 
    "✍️ Submissão de Trabalhos", 
    "🔍 Consultar Status do Trabalho", 
    "🎓 Certificados", 
    "💳 Taxa de DOI Individual", 
    "📚 Anais Publicados"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    st.subheader("Bem-vindo ao Portal de Eventos Científicos da FST da PUC Goiás")
    st.write("Central oficial de gestão acadêmica, submissão de resumos, acompanhamento de avaliação, emissão de certificados e publicação de anais.")
    st.markdown("""
    * **Inscrições:** Gratuitas para PUC Goiás / Pagas (Standby) para externos mediante envio de comprovante.
    * **Submissões:** Realizadas via formulário específico com normas detalhadas por modalidade.
    * **Certificados:** Disponíveis para ouvintes (20h), apresentadores (5h) e membros da banca avaliadora.
    """)

# --- 2. EVENTOS E INSCRIÇÕES (MÚLTIPLOS EVENTOS) ---
elif menu == "🎟️ Eventos e Inscrições":
    st.subheader("🎟️ Programação de Eventos e Cursos Disponíveis")
    st.write("Selecione abaixo o evento de seu interesse para ver os detalhes, normas e realizar a inscrição.")
    
    evento_selecionado = st.selectbox("Escolha o Evento:", [
        "1. Jornada Científica do Curso de Fisioterapia", 
        "2. Minicurso Prático: Reabilitação e Terapia Manual", 
        "3. Workshop: Inovação e Tecnologias em Saúde",
        "4. Simpósio de Saúde Coletiva e Políticas Públicas"
    ])
    
    st.markdown("---")
    
    if "Jornada Científica" in evento_selecionado:
        st.markdown("### 🩺 Jornada Científica do Curso de Fisioterapia")
        st.write("""
        * **Público-alvo:** Estudantes, docentes, profissionais e pesquisadores.
        * **Investimento:** 
          * Estudantes, Docentes e Banca da PUC Goiás: **Gratuito**.
          * Participantes Externos (Estudantes, Docentes e Profissionais): **R$ 10,00** (Standby mediante comprovante na chave `eventoscientificospucgoias@hotmail.com`).
        * **Destaque:** Permite submissão de Resumos Simples, Expandidos e Artigos Completos com ISBN gratuito.
        """)
        
        st.markdown("### **EIXOS TEMÁTICOS**")
        st.markdown("""
        * Fisioterapia Ortopédica, Reumatológica, Traumatológica e Desportiva
        * Fisioterapia em Terapia Intensiva e Cardiorrespiratória
        * Fisioterapia Neurológica e Pediátrica
        * Saúde da Mulher, Pélvica e Oncológica
        * Saúde Coletiva, Políticas Públicas e Inovação em Saúde
        * Tecnologias Digitais e Inteligência Artificial na Saúde
        * Outras Áreas
        """)
        
        st.warning("⚠️ **Atenção para inscrições pagas:** Ficarão em status de **Standby (Aguardando Confirmação)** até que a equipe financeira valide o comprovante de PIX enviado no formulário em relação à chave: `eventoscientificospucgoias@hotmail.com`.")
        st.write("")
        st.link_button("🔗 Inscrever-se na Jornada Científica", "https://forms.gle/4bSypbzykj1FEpR4A")
        st.caption("Após o envio, sua inscrição será processada pela organização.")
        
    elif "Minicurso Prático" in evento_selecionado:
        st.markdown("### 🤲 Minicurso Prático: Reabilitação e Terapia Manual")
        st.write("""
        * **Carga Horária:** 4 horas práticas.
        * **Investimento:** R$ 30,00 (Vagas limitadas). Pagamento via PIX para `eventoscientificospucgoias@hotmail.com`.
        * **Certificação:** Certificado emitido pela Pró-Reitoria de Extensão da PUC Goiás.
        """)
        st.link_button("🔗 Inscrever-se no Minicurso Prático", "https://forms.gle/SEU_LINK_DO_MINICURSO_AQUI")
        
    elif "Workshop" in evento_selecionado:
        st.markdown("### 💡 Workshop: Inovação e Tecnologias em Saúde")
        st.write("""
        * **Foco:** Discussão sobre inteligência artificial, teleatendimento e novas tecnologias reabilitadoras.
        * **Investimento:** Gratuito para toda a comunidade acadêmica.
        """)
        st.link_button("🔗 Inscrever-se no Workshop", "https://forms.gle/SEU_LINK_DO_WORKSHOP_AQUI")
        
    elif "Simpósio" in evento_selecionado:
        st.markdown("### 📊 Simpósio de Saúde Coletiva e Políticas Públicas")
        st.write("""
        * **Foco:** Mesas-redondas e debates sobre o SUS e gestão em saúde.
        * **Investimento:** Gratuito.
        """)
        st.link_button("🔗 Inscrever-se no Simpósio", "https://forms.gle/SEU_LINK_DO_SIMPOSIO_AQUI")

# --- 3. SUBMISSÃO DE TRABALHOS ---
elif menu == "✍️ Submissão de Trabalhos":
    st.subheader("✍️ Central de Submissão de Trabalhos Científicos")
    st.write("Consulte abaixo as normas e utilize o link do formulário exclusivo para enviar o seu arquivo Word (.doc/.docx).")
    
    tab_simples, tab_expandido, tab_completo = st.tabs(["📄 Resumo Simples", "📑 Resumo Expandido", "📚 Artigo Completo"])
    
    with tab_simples:
        st.markdown("### Normas para Submissão de Resumo Simples")
        st.markdown("""
        * **Estrutura Obrigatória:** Introdução, Objetivos, Metodologia, Resultados e Discussão, e Considerações Finais.
        * **Formatação:** Mínimo de 250 palavras e Máximo de 350 palavras. Fonte Times New Roman, tamanho 12, espaçamento 1,0.
        """)
    with tab_expandido:
        st.markdown("### Normas para Submissão de Resumo Expandido")
        st.markdown("""
        * **Extensão:** No mínimo 4 páginas e no máximo 7 páginas completas.
        """)
    with tab_completo:
        st.markdown("### Normas para Submissão de Artigo Completo")
        st.markdown("""
        * **Extensão:** No mínimo 8 páginas e no máximo 16 páginas completas.
        """)

    st.markdown("---")
    st.link_button("📥 Clique aqui para acessar o Formulário de Submissão de Trabalhos", "https://forms.gle/wqFaFTRRxj2KwKsp9")

# --- 4. CONSULTAR STATUS DO TRABALHO ---
elif menu == "🔍 Consultar Status do Trabalho":
    st.subheader("🔍 Acompanhamento de Avaliação do Trabalho")
    st.write("Digite o seu e-mail cadastrado na submissão para verificar o parecer atual da comissão científica.")
    
    with st.form("form_status"):
        email_busca = st.text_input("Digite o seu E-mail cadastrado:").strip().lower()
        consultar = st.form_submit_button("Consultar Status")
        
        if consultar:
            if email_busca:
                st.markdown("---")
                st.info(f"🔎 Buscando parecer para o e-mail: **{email_busca}**")
                
                try:
                    import pandas as pd
                    link_planilha = "https://docs.google.com/spreadsheets/d/1wBmZZI6-6WwmrrNsb0L6d2-iyPCZ2WGQUM1xzsylBu8/edit?usp=sharing"
                    
                    if "/edit" in link_planilha:
                        id_planilha = link_planilha.split("/d/")[1].split("/")[0]
                        url_csv = f"https://docs.google.com/spreadsheets/d/{id_planilha}/export?format=csv"
                    else:
                        url_csv = link_planilha
                    
                    df = pd.read_csv(url_csv)
                    coluna_email = None
                    for col in df.columns:
                        if 'e-mail' in col.lower() or 'email' in col.lower() or 'endereço' in col.lower():
                            coluna_email = col
                            break
                    
                    if coluna_email:
                        df[coluna_email] = df[coluna_email].astype(str).str.strip().str.lower()
                        resultado = df[df[coluna_email] == email_busca]
                        
                        if not resultado.empty:
                            coluna_status = None
                            for col in df.columns:
                                if 'status' in col.lower():
                                    coluna_status = col
                                    break
                            
                            if coluna_status:
                                status_trabalho = str(resultado.iloc[0][coluna_status]).strip().capitalize()
                                if "Análise" in status_trabalho:
                                    st.warning("⏳ **Status:** Recebido / Em Análise.")
                                elif "Aprovado" in status_trabalho:
                                    st.success("🎉 **Status:** APROVADO!")
                                elif "Correções" in status_trabalho:
                                    st.error("⚠️ **Status:** Solicitação de Alterações Pendentes.")
                                else:
                                    st.info(f"📌 **Status:** {status_trabalho}")
                            else:
                                st.error("Coluna 'Status' não encontrada na planilha.")
                        else:
                            st.warning("Nenhum trabalho encontrado para este e-mail.")
                    else:
                        st.error("Coluna de e-mail não identificada.")
                except Exception as e:
                    st.error("Erro ao ler a planilha.")
            else:
                st.error("Por favor, digite um e-mail válido.")

# --- 5. CERTIFICADOS ---
elif menu == "🎓 Certificados":
    st.subheader("🎓 Emissão e Consulta de Certificados")
    st.write("Selecione a sua categoria abaixo para emitir ou validar o seu certificado oficial do evento.")
    
    tipo_certificado = st.selectbox("Escolha a Categoria do Certificado:", [
        "1. Certificado de Ouvinte (Carga Horária: 20h)",
        "2. Certificado de Apresentador de Trabalho (Carga Horária: 5h)",
        "3. Certificado de Membro da Banca Avaliadora"
    ])
    
    st.markdown("---")
    
    if "Ouvinte" in tipo_certificado:
        st.markdown("### 📜 Certificado de Participação (Ouvinte - 20h)")
        st.write("Insira o seu e-mail cadastrado na lista de presença para emitir o certificado de 20 horas.")
        with st.form("form_cert_ouvinte"):
            email_ouvinte = st.text_input("E-mail cadastrado na presença:")
            btn_ouvinte = st.form_submit_button("Gerar Certificado de Ouvinte")
            if btn_ouvinte:
                if email_ouvinte:
                    st.success("✅ Presença confirmada!")
                    st.download_button("📥 Baixar Certificado em PDF", data="Certificado Fictício Ouvinte 20h", file_name="certificado_ouvinte_20h.pdf")
                else:
                    st.error("Digite o e-mail.")
                    
    elif "Apresentador" in tipo_certificado:
        st.markdown("### 📜 Certificado de Apresentador de Trabalho (5h)")
        st.write("Certificado emitido para autores que apresentaram trabalhos científicos na Jornada (5 horas complementares).")
        with st.form("form_cert_apresentador"):
            email_apresentador = st.text_input("E-mail do autor apresentador:")
            btn_apresentador = st.form_submit_button("Gerar Certificado de Apresentador")
            if btn_apresentador:
                if email_apresentador:
                    st.success("✅ Trabalho validado para apresentação!")
                    st.download_button("📥 Baixar Certificado de Apresentador (5h)", data="Certificado Fictício Apresentador 5h", file_name="certificado_apresentador_5h.pdf")
                else:
                    st.error("Digite o e-mail.")
                    
    elif "Banca Avaliadora" in tipo_certificado:
        st.markdown("### 📜 Certificado de Membro da Banca Avaliadora")
        st.write("Certificado oficial para os professores e avaliadores da banca examinadora.")
        st.info("ℹ️ *O certificado conterá o título do trabalho avaliado, o nome do aluno autor, o nome do orientador e dos membros da banca.*")
        with st.form("form_cert_banca"):
            email_banca = st.text_input("E-mail do Membro da Banca:")
            btn_banca = st.form_submit_button("Gerar Certificado da Banca")
            if btn_banca:
                if email_banca:
                    st.success("✅ Participação na Banca Validada!")
                    st.markdown("""
                    * **Trabalho Avaliado:** Efeito da Reabilitação Vestibular na Qualidade de Vida (Exemplo)
                    * **Aluno(a):** Maria da Silva
                    * **Orientador(a):** Prof. Dr. Carlos Alberto
                    * **Membros da Banca:** Prof. Dr. Carlos Alberto, Profa. Ma. Larissa (Você) e Prof. Dr. João Pedro.
                    """)
                    st.download_button("📥 Baixar Certificado da Banca Avaliadora", data="Certificado Fictício Banca", file_name="certificado_banca_avaliadora.pdf")
                else:
                    st.error("Digite o e-mail.")

# --- 6. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("A publicação nos Anais oficiais com ISBN é gratuita. O DOI individual é opcional (R$ 15,00).")
    st.info("ℹ️ **Chave PIX:** eventoscientificospucgoias@hotmail.com")
    
    with st.form("form_doi"):
        id_trabalho = st.text_input("Título Exato do Trabalho Aprovado")
        comprovante_doi = st.file_uploader("Anexe o Comprovante do PIX da Taxa de DOI", type=["pdf", "png", "jpg"])
        if st.form_submit_button("Requisitar DOI"):
            if id_trabalho and comprovante_doi:
                st.success("Comprovante enviado! Em até 1 semana o DOI será emitido.")
            else:
                st.error("Preencha os campos obrigatórios.")

# --- 7. ANAIS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Repositório Oficial de Anais")
    st.write("Acesse abaixo os cadernos de resumos e anais oficiais da Jornada Científica de Fisioterapia da PUC Goiás.")
    st.markdown("---")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write("**Anais da Jornada Científica do Curso de Fisioterapia — PUC Goiás (2026)**")
        st.caption("Publicado oficialmente | ISBN: 0000-0000 (Exemplo)")
    with col2:
        st.link_button("📥 Baixar Anais", "https://drive.google.com/file/d/19ysTkH8FBmHI4F4MzmRKynaVcmX6EmQH/view?usp=drive_link")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Tecnologias • Saúde e Sociedade FST Fisioterapia | PUC Goiás</p>", unsafe_allow_html=True)
