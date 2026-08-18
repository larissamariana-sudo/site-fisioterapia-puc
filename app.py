import streamlit as st
import pandas as pd

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
    
    cat = st.radio("Selecione a opção desejada:", [
        "Participante/Ouvinte", "Apresentador de Trabalho", "Membro da Banca", "Cadastro de Trabalho para Certificação (Orientador)"
    ])
    
    if cat == "Participante/Ouvinte":
        st.link_button("🔗 Inscrever-se como Ouvinte", "https://forms.gle/Vcrdj9e8KJQ9Qqo76")
    elif cat == "Apresentador de Trabalho":
        st.link_button("🔗 Inscrever-se como Apresentador", "https://forms.gle/mgLc9iaibDfBYqi78")
    elif cat == "Membro da Banca":
        st.link_button("🔗 Inscrever-se como Banca", "https://forms.gle/mgLc9iaibDfBYqi78")
    else:
        st.info("⚠️ **Exclusivo para Orientadores:** Utilize este formulário para cadastrar o trabalho, estudante e banca para o certificado.")
        st.link_button("📝 Cadastrar Informações do Trabalho", "https://forms.gle/bTGR48dU3rrgBgr17")

# --- 3. TRABALHOS (SUBMISSÃO + STATUS) ---
elif menu == "✍️ Trabalhos Científicos":
    st.subheader("✍️ Central de Trabalhos Científicos")
    tab1, tab2 = st.tabs(["📥 Submissão e Normas", "🔍 Consultar Status"])
    st.write("Consulte abaixo as normas e utilize o link do formulário exclusivo para enviar o seu arquivo Word (.doc/.docx).")
    
    tab_simples, tab_expandido, tab_completo = st.tabs(["📄 Resumo Simples", "📑 Resumo Expandido", "📚 Artigo Completo"])
    
    with tab_simples:
        st.markdown("### Normas para Submissão de Resumo Simples")
        st.markdown("* **Estrutura Obrigatória:** Introdução, Objetivos, Metodologia, Resultados e Discussão, e Considerações Finais.
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
        st.markdown("
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
        st.markdown("
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

    tab1, tab2 = st.tabs(["📥 Submissão", "🔍 Consultar Status"])
    
    with tab1:
        st.write("Envie seu arquivo Word (.doc/.docx) via formulário.")
        st.link_button("📥 Acessar Formulário de Submissão", "LINK_SUBMISSAO")
        
    with tab2:
        st.write("Consulte o parecer da comissão científica.")
        CONSULTAR STATUS DO TRABALHO ---
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

# --- 4. CERTIFICADOS (EMISSÃO + VALIDAÇÃO) ---
elif menu == "🎓 Certificados e Validação":
    st.subheader("🎓 Certificados")
    tab1, tab2 = st.tabs(["📜 Emitir Certificado", "🛡️ Validar Autenticidade"])
    with tab1:
        st.selectbox("Categoria:", ["Ouvinte (16h)", "Apresentador (5h)", "Banca Avaliadora"])
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
    st.link_button("📥 Baixar Anais", "COLE_LINK_PDF_ANAIS_AQUI")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Tecnologias • Saúde e Sociedade FST Fisioterapia | PUC Goiás</p>", unsafe_allow_html=True)
