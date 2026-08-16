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
    "🔍 Consultar Status do Trabalho", 
    "💳 Taxa de DOI Individual", 
    "📚 Anais Publicados"
])

# --- 1. INÍCIO ---
if menu == "🏠 Início / Sobre":
    st.subheader("Bem-vindo ao Portal de Eventos Científicos da FST da PUC Goiás")
    st.write("Central oficial de gestão acadêmica, submissão de resumos, acompanhamento de avaliação e publicação de anais.")
    st.markdown("""
    * **Inscrições:** Gratuitas para PUC Goiás / Pagas (Standby) para externos mediante envio de comprovante.
    * **Submissões:** Realizadas via formulário específico com normas detalhadas por modalidade.
    * **Avaliação:** Acompanhe em tempo real se seu trabalho está em análise, aprovado ou pendente de correções.
    """)

# --- 2. INSCRIÇÕES ---
elif menu == "🎟️ Inscrições (Eventos)":
    st.subheader("🎟️ Inscrição na Jornada Científica do Curso de Fisioterapia")
    st.write("""
        * **Estudantes, Docentes e Banca da PUC Goiás:** Inscrição totalmente **Gratuita**.
        * **Participantes Externos (Estudantes, Docentes e Profissionais):** Inscrição **Paga (R$ 10,00)**. 
        * **Possibilidade de submissão de resumos simples/resumos expandidos/artigos completos com ISBN GRATUITO**
        * **EIXOS TEMÁTICOS**
            
            Fisioterapia Ortopédica, Reumatológica, Traumatológica e Desportiva,
            
            Fisioterapia em Terapia Intensiva e Cardiorrespiratória,
            
            Fisioterapia Neurológica e Pediátrica,
            
            Saúde da Mulher, Pélvica e Oncológica,
            
            Saúde Coletiva, Políticas Públicas e Inovação em Saúde,
            
            Tecnologias Digitais e Inteligência Artificial na Saúde

            Outras Áreas
            
        ⚠️ **Atenção para inscrições pagas:** Ficarão em status de **Standby (Aguardando Confirmação)** até que a equipe financeira valide o comprovante de PIX enviado no formulário em relação à chave: `eventoscientificospucgoias@hotmail.com`.
    """)
    st.write("")
    st.link_button("🔗 Clique aqui para preencher o formulário oficial de inscrição", "https://forms.gle/4bSypbzykj1FEpR4A")
    st.caption("Após o envio, sua inscrição será processada pela organização.")

# --- 3. SUBMISSÃO DE TRABALHOS ---
elif menu == "✍️ Submissão de Trabalhos":
    st.subheader("✍️ Central de Submissão de Trabalhos Científicos")
    st.write("Consulte abaixo as normas e utilize o link do formulário exclusivo para enviar o seu arquivo Word (.doc/.docx).")
    
    tab_simples, tab_expandido, tab_completo = st.tabs(["📄 Resumo Simples", "📑 Resumo Expandido", "📚 Artigo Completo"])
    
    with tab_simples:
        st.markdown("### Normas para Submissão de Resumo Simples")
        st.write("250 a 350 palavras. Formato Word. Estrutura: Introdução, Objetivos, Metodologia, Resultados e Discussão, Considerações Finais.")
        
        **INFORMAÇÕES PARA A SUBMISSÃO**
        
        **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
        
        **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
        
        **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
        
        **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.

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
        st.write("4 a 7 páginas. Formato Word. Seguindo as normas da ABNT.")
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
        * **Instituição:** 1;2 Pontifícia Universidade Católica de Goiás.
        """)
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
        st.write("8 a 16 páginas. Formato Word. Comprovante de Comitê de Ética quando aplicável.")
        
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

        * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
        * **Extensão:** No mínimo 8 páginas e no máximo 16 páginas completas.
        * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
        * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
        * **Citações e Referências:** Devem seguir as normas da ABNT (NBR 10520:2023 e NBR 6023:2023).
        * **Figuras e Tabelas:** Permitido até 2 elementos ilustrativos inseridos no corpo do texto.
        """)

    st.markdown("---")
    st.info("📌 **Importante:** Para que os arquivos sejam salvos diretamente na nuvem da comissão científica e organizados em planilhas, a submissão é feita por formulário dedicado.")
    
    # BOTÃO PARA O SEGUNDO GOOGLE FORMS (SUBMISSÃO)
    st.link_button("📥 Clique aqui para acessar o Formulário de Submissão de Trabalhos", "https://forms.gle/wqFaFTRRxj2KwKsp9")

# --- 4. CONSULTAR STATUS DO TRABALHO ---
elif menu == "🔍 Consultar Status do Trabalho":
    st.subheader("🔍 Acompanhamento de Avaliação do Trabalho")
    st.write("Digite o seu e-mail de cadastro ou o código/título do trabalho para verificar em qual etapa de avaliação ele se encontra.")
    
    with st.form("form_status"):
        busca = st.text_input("E-mail do autor principal ou Título do trabalho:")
        consultar = st.form_submit_button("Consultar Status")
        
        if consultar:
            if busca:
                # Simulação visual inteligente do status acadêmico
                st.markdown("---")
                st.info(f"🔎 Resultado da busca para: **{busca}**")
                st.success("✅ **Status Atual:** Em Avaliação pela Banca Científica")
                st.markdown("""
                * **Etapas possíveis no sistema:**
                  * ⏳ *Recebido / Em Análise:* O trabalho foi entregue e repassado aos avaliadores.
                  * ✅ *Aprovado:* Trabalho aceito para apresentação e publicação nos Anais!
                  * ⚠️ *Solicitação de Alterações:* O comitê científico retornou com apontamentos de ajustes necessários no texto. Verifique seu e-mail cadastrado.
                """)
            else:
                st.error("Por favor, digite um e-mail ou título válido para consulta.")

# --- 5. DOI ---
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

# --- 6. ANAIS ---
elif menu == "📚 Anais Publicados":
    st.subheader("📚 Repositório Oficial de Anais")
    st.write("Aqui ficarão disponíveis os cadernos de resumos e anais oficiais do evento assim que forem publicados e indexados com ISBN.")
    st.markdown("---")
    
    # Exemplo de link de visualização e download dos Anais
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write("**Anais da Jornada Científica do Curso de Fisioterapia — PUC Goiás (2026)**")
        st.caption("Status: Em preparação para publicação pós-evento (ISBN: 0000-0000)")
    with col2:
        # Quando publicados, substitua o link '#' pelo link direto do PDF no Google Drive
        st.link_button("📥 Baixar Anais", "#", disabled=True)

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Tecnologias • Saúde e Sociedade FST Fisioterapia | PUC Goiás</p>", unsafe_allow_html=True)
