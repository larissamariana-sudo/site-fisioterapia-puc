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
        * **Encerrado; em breve nova turma**
        * **Carga Horária:** 4 horas práticas.
        * **Investimento:** R$ 30,00 (Vagas limitadas). Pagamento via PIX para `eventoscientificospucgoias@hotmail.com`.
        * **Certificação:** Certificado emitido pela Pró-Reitoria de Extensão da PUC Goiás.
        """)
        st.link_button("🔗 Inscrever-se no Minicurso Prático", "https://forms.gle/SEU_LINK_DO_MINICURSO_AQUI")
        
    elif "Workshop" in evento_selecionado:
        st.markdown("### 💡 Workshop: Inovação e Tecnologias em Saúde")
        st.write("""
        * **Em breve**
        * **Foco:** Discussão sobre inteligência artificial, teleatendimento e novas tecnologias reabilitadoras.
        * **Investimento:** Gratuito para toda a comunidade acadêmica.
        """)
        st.link_button("🔗 Inscrever-se no Workshop", "https://forms.gle/SEU_LINK_DO_WORKSHOP_AQUI")
        
    elif "Simpósio" in evento_selecionado:
        st.markdown("### 📊 Debate Saúde Coletiva e Políticas Públicas")
        st.write("""
        * **Encerradas as inscrições**
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
        * **Formatação:** Mínimo de 250 palavras e Máximo de 350 palavras (excluindo título e referências). Fonte Times New Roman, tamanho 12, espaçamento 1,0.
        * **Palavras-chave:** De 3 a 5 palavras-chave separadas por ponto e vírgula.
        * **Autores:** Permitido até 3 autores por trabalho (incluindo o orientador).
        
        **INFORMAÇÕES PARA A SUBMISSÃO**
        * **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
        * **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
        * **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
        * **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
        
        **INSTRUÇÕES DE FORMATAÇÃO OBRIGATÓRIAS**
        * **Espaçamento:** Entre os tópicos/seções do seu trabalho, inserir uma linha em branco. 
        * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
        * **Alinhamento:** Justificado.
        * **Título:** Alinhado à esquerda, em caixa alta e negrito.
        * **Autores:** Primeiro nome (acadêmico); segundo nome (orientador). Escritos de forma corrida, separados por ponto e vírgula, em caixa alta. Ex.: Maria de Oliveira1; Antônio da Silva2.
        * **Instituição:** 1;2 Pontifícia Universidade Católica de Goiás.
        """)
        st.info("💡 Ideal para resumos de trabalhos que exigem ineditismo, relatos de experiência, pesquisas em andamento ou revisões bibliográficas preliminares.")
    
    with tab_expandido:
        st.markdown("### Normas para Submissão de Resumo Expandido")
        st.markdown("""
        * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
        * **Extensão:** No mínimo 4 páginas e no máximo 7 páginas completas.
        * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
        * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
        * **Citações e Referências:** Devem seguir as normas da ABNT (NBR 10520:2023 e NBR 6023:2023).
        * **Figuras e Tabelas:** Permitido até 2 elementos ilustrativos inseridos no corpo do texto.
        
        **INFORMAÇÕES PARA A SUBMISSÃO**
        * **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
        * **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
        * **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
        * **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
        """)
        st.info("💡 Indicado para artigos científicos e pesquisas finalizadas que necessitam de um detalhamento metodológico maior.")
               
    with tab_completo:
        st.markdown("### Normas para Submissão de Artigo Completo")
        st.markdown("""
        * **Estrutura Obrigatória:** Resumo, Palavras-chave, Introdução, Metodologia, Resultados e Discussão, Conclusão, Referências Bibliográficas.
        * **Extensão:** No mínimo 8 páginas e no máximo 16 páginas completas.
        * **Formatação:** Fonte Times New Roman, tamanho 12, espaçamento entre linhas 1,0, recuo de parágrafo de 1,25 cm.
        * **Margens:** Superior e esquerda de 3 cm; inferior e direita de 2 cm.
        * **Citações e Referências:** Devem seguir as normas da ABNT (NBR 10520:2023 e NBR 6023:2023).
        * **Figuras e Tabelas:** Permitido até 2 elementos ilustrativos inseridos no corpo do texto.
        
        **INFORMAÇÕES PARA A SUBMISSÃO**
        * **Formato:** Todos os trabalhos devem ser submetidos obrigatoriamente em arquivo formato WORD.
        * **Prazo:** As submissões devem ser realizadas estritamente dentro das datas estabelecidas no cronograma oficial.
        * **Gratuidade:** A submissão e a publicação nos anais do evento são totalmente gratuitas (ISBN).
        * **DOI (Opcional):** Autores que desejarem maior rastreabilidade podem optar pela aquisição do registro de DOI.
        """)

    st.markdown("---")
    st.info("📌 **Importante:** Para que os arquivos sejam salvos diretamente na nuvem da comissão científica e organizados em planilhas, a submissão é feita por formulário dedicado.")
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
                        col_limpa = col.strip().lower()
                        if 'e-mail' in col_limpa or 'email' in col_limpa or 'endereço' in col_limpa:
                            coluna_email = col
                            break
                    
                    if coluna_email:
                        df[coluna_email] = df[coluna_email].astype(str).str.strip().str.lower()
                        resultado = df[df[coluna_email] == email_busca]
                        
                        if not resultado.empty:
                            coluna_status = None
                            for col in df.columns:
                                col_limpa = col.strip().lower()
                                if 'status' in col_limpa:
                                    coluna_status = col
                                    break
                            
                            if coluna_status:
                                status_trabalho = str(resultado.iloc[0][coluna_status]).strip().capitalize()
                                
                                if "Análise" in status_trabalho or "Em análise" in status_trabalho:
                                    st.warning("⏳ **Status Atual:** Recebido / Em Análise pela Banca Científica.")
                                    st.write("Seu trabalho foi entregue e está passando pela avaliação dos pares. Acompanhe seu e-mail.")
                                    
                                elif "Aprovado" in status_trabalho:
                                    st.success("🎉 **Status Atual:** APROVADO!")
                                    st.write("Parabéns! Seu trabalho foi aceito para apresentação e publicação nos Anais oficiais do evento.")
                                    
                                elif "Correções" in status_trabalho or "Correção" in status_trabalho:
                                    st.error("⚠️ **Status Atual:** Solicitação de Alterações Pendentes.")
                                    st.markdown("""
                                    O comitê científico revisou seu trabalho e solicitou ajustes estruturais ou textuais. 
                                    * **O que fazer:** Verifique as orientações enviadas para o seu e-mail de cadastro, faça as alterações necessárias no arquivo Word e reenvie a nova versão conforme as instruções da comissão.
                                    """)
                                else:
                                    st.info(f"📌 **Status Atual:** {status_trabalho}")
                            else:
                                st.error("Atenção: Não foi encontrada nenhuma coluna chamada 'Status' na sua planilha. Certifique-se de criar uma coluna com o nome exato 'Status'.")
                        else:
                            st.warning("Nenhum trabalho encontrado para este e-mail. Verifique se digitou o mesmo e-mail utilizado no momento da submissão.")
                    else:
                        st.error(f"Não foi possível identificar a coluna de e-mail. Colunas encontradas na sua planilha: {list(df.columns)}")
                        
                except Exception as e:
                    st.error(f"Erro ao ler a planilha: {e}. Certifique-se de que a planilha está compartilhada como 'Qualquer pessoa com o link pode ser leitor'.")
            else:
                st.error("Por favor, digite um e-mail válido para realizar a consulta.")

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
