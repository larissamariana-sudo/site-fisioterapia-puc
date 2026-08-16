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
    st.subheader("Bem-vindo ao Portal de Eventos Científicos da FST da PUC Goiás")
    
    st.write("""
        Este portal foi desenvolvido para centralizar a gestão acadêmica e científica do nosso curso. 
        Aqui, estudantes, professores, pesquisadores e profissionais encontram um espaço integrado para:
    """)
    
    st.markdown("""
    * **Inscrições** em jornadas, simpósios, palestras e minicursos;
    * **Submissão de Trabalhos** (Resumos Simples, Expandidos e Artigos Completos) divididos por eixos temáticos;
    * **Emissão Opcional de DOI Individual** para artigos aprovados, garantindo maior visibilidade acadêmica (Lattes e Pós-Graduação);
    * **Repositório Oficial de Anais** com edições anteriores publicadas com ISBN.
    """)
    
    st.info("💡 **Navegue pelo menu lateral** para realizar suas inscrições, conferir as normas vigentes e acompanhar a programação dos nossos eventos!")

# --- 2. INSCRIÇÕES ---
elif menu == "🎟️ Inscrições (Eventos)":
    st.subheader("🎟️ Inscrição na Jornada Científica do Curso de Fisioterapia")
    st.write("""
        **As inscrições no evento para banca examinadora, estudantes e docentes da PUC Goiás, são GRATUITAS.**
        
        As inscrições no evento para externos (estudantes, docentes e profissionais - categorias externas) são confirmadas após o pagamento da taxa de inscrição e envio do comprovante de pagamento através do formulário integrado.
    """)    
    st.write("")
    
    st.link_button("🔗 Clique aqui para preencher o formulário oficial de inscrição", "https://forms.gle/4bSypbzykj1FEpR4A")
    
    st.write("")
    st.caption("Após o envio pelo formulário, sua inscrição será processada e registrada automaticamente no sistema da organização.")

# --- 3. SUBMISSÃO DE TRABALHOS ---
elif menu == "✍️ Submissão de Trabalhos":
    st.subheader("✍️ Central de Submissão de Trabalhos Científicos")
    st.write("Consulte abaixo as normas e instruções para cada modalidade antes de realizar o envio do seu arquivo.")
    
    tab_simples, tab_expandido, tab_completo = st.tabs(["📄 Resumo Simples", "📑 Resumo Expandido", "📚 Artigo Completo"])
    
    with tab_simples:
        st.markdown("### Normas para Submissão de Resumo Simples")
        st.write("""
        * **Estrutura Obrigatória:** Introdução, Objetivos, Metodologia, Resultados e Discussão, e Considerações Finais.
        * **Formatação:** Mínimo de 250 palavras e Máximo de 350 palavras (excluindo título e referências). Fonte Times New Roman, tamanho 12, espaçamento 1,0.
        * **Palavras-chave:** De 3 a 5 palavras-chave separadas por ponto e vírgula.
        * **Autores:** Permitido até 3 autores por trabalho (incluindo o orientador).
        
        **INFORMAÇÕES PARA A SUBMISSÃO**
        
        **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
        
        **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
        
        **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
        
        **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
        
        **INSTRUÇÕES DE FORMATAÇÃO OBRIGATÓRIAS**
        
        * **Espaçamento:** Entre os tópicos/seções do seu trabalho, inserir uma linha em branco. 
        * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
        * **Alinhamento:** Justificado.
        * **Título:** Alinhado à esquerda, em caixa alta e negrito.
        * **Autores:** Primeiro nome (acadêmico); segundo nome (orientador). Escritos de forma corrida, separados por ponto e vírgula, em caixa alta. Ex.: Maria de Oliveira1; Antônio da Silva2.
        * **Instituição:** 1;2Pontifícia Universidade Católica de Goiás.
        """)
        st.info("💡 Ideal para resumos de trabalhos que exigem ineditismo, relatos de experiência, pesquisas em andamento ou revisões bibliográficas preliminares.")

    with tab_expandido:
        st.markdown("### Normas para Submissão de Resumo Expandido")
        st.write("""
        * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
        * **Extensão:** No mínimo 4 páginas e no máximo 7 páginas completas.
        * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
        * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
        * **Citações e Referências:** Devem seguir as normas da ABNT (NBR 10520:2023 e NBR 6023:2023).
        * **Figuras e Tabelas:** Permitido até 2 elementos ilustrativos inseridos no corpo do texto.
        """)
        st.info("💡 Indicado para artigos científicos e pesquisas finalizadas que necessitam de um detalhamento metodológico maior.")

    with tab_completo:
        st.markdown("### Normas para Submissão de Artigo Completo")
        st.write("""
        * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
        * **Extensão:** No mínimo 8 páginas e no máximo 16 páginas completas.
        * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
        * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
        * **Citações e Referências:** Devem seguir as normas da ABNT (NBR 10520:2023 e NBR 6023:2023).
        * **Figuras e Tabelas:** Permitido até 2 elementos ilustrativos inseridos no corpo do texto.
        """)

    st.markdown("---")
    
    with st.form("form_submissao_trabalho"):
        modalidade = st.selectbox("Selecione a Modalidade de Submissão:", [
            "Resumo Simples",
            "Resumo Expandido",
            "Artigo Completo"
        ])
        
        titulo_trab = st.text_input("Título do Trabalho")
        autor_princ = st.text_input("Autor Principal (Apresentador)")
        coautores = st.text_area("Coautores (separados por vírgula)")
        
        categoria = st.selectbox("Selecione a Categoria / Eixo Temático:", [
            "Fisioterapia Ortopédica, Reumatológica, Traumatológica e Desportiva",
            "Fisioterapia em Terapia Intensiva e Cardiorrespiratória",
            "Fisioterapia Neurológica e Pediátrica",
            "Saúde da Mulher, Pélvica e Oncológica",
            "Saúde Coletiva, Políticas Públicas e Inovação em Saúde",
            "Tecnologias Digitais e Inteligência Artificial na Saúde",
            "Outras Áreas"
        ])
        
        arquivo_resumo = st.file_uploader("Anexe o arquivo correspondente (Formato Word .doc ou .docx)", type=["doc", "docx"])
        
        btn_submeter = st.form_submit_button("Enviar Trabalho para Avaliação")
        if btn_submeter:
            if titulo_trab and autor_princ and arquivo_resumo:
                st.success(f"Trabalho ({modalidade}) submetido com sucesso na categoria **{categoria}**! O seu protocolo de rastreio foi gerado.")
            else:
                st.error("Por favor, preencha todos os campos obrigatórios e anexe o arquivo correto.")

# --- 4. DOI ---
elif menu == "💳 Taxa de DOI Individual":
    st.subheader("💳 Solicitação e Pagamento de DOI Individual")
    st.write("A publicação nos Anais oficiais com ISBN é gratuita. O DOI individual é opcional.")
    st.info("ℹ️ **Valor:** R$ 15,00. **Chave PIX:** eventoscientificospucgoias@hotmail.com")
    
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
st.markdown("<p style='text-align: center; color: gray;'>Tecnologias • Saúde e Sociedade FST Fisioterapia</p>", unsafe_allow_html=True)
