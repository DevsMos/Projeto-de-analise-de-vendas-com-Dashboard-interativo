Documentação do Código Python

Importações:

    streamlit: Biblioteca para criar interfaces web interativas.
    pandas: Biblioteca para manipulação de dados em formato tabular.
    plotly.express: Biblioteca para criação de gráficos interativos.
    openpyxl: Biblioteca para leitura e escrita de arquivos Excel.

Configuração da Página:

    st.set_page_config("WIDE"): Define o layout da página como "amplo", proporcionando mais espaço para os gráficos.

Leitura do Arquivo Excel:

    df1 = pd.read_excel("Plan_vendas.xlsx", sheet_name="Plan", usecols="A:K", header=0):
        Lê o arquivo Excel "Plan_vendas.xlsx".
        Utiliza a planilha "Plan" como fonte de dados.
        Importa as colunas de "A" a "K".
        Assume a primeira linha como cabeçalho dos dados.
    Armazena os dados em um DataFrame chamado df1.

Tratamento dos Dados:

    df1["Data Emissão Pedido"] = pd.to_datetime(df1["Data Emissão Pedido"]):
        Converte a coluna "Data Emissão Pedido" para o formato de data.
    df1 = df1.sort_values("Data Emissão Pedido"):
        Ordena o DataFrame por "Data Emissão Pedido" em ordem crescente.
    df1["Data Emissão Pedido"] = df1["Data Emissão Pedido"].apply(lambda x: str(x.year) + "-" + str(x.month)):
        Cria uma nova coluna "Data Emissão Pedido" que contém o ano e o mês da data original.

Seleção de Filtros:

    month = st.sidebar.selectbox("Selecione Produto", df1["Produto"].unique()):
        Cria um menu suspenso na barra lateral para selecionar o "Produto".
        As opções disponíveis são os valores únicos presentes na coluna "Produto" do DataFrame.
    prod = st.sidebar.selectbox("Selecione o Estado",df1["Estado"].unique()):
        Cria um menu suspenso na barra lateral para selecionar o "Estado".
        As opções disponíveis são os valores únicos presentes na coluna "Estado" do DataFrame.
    cliente = st.sidebar.selectbox("Selecione Cliente",df1["Canal de Vendas"].unique()):
        Cria um menu suspenso na barra lateral para selecionar o "Canal de Vendas".
        As opções disponíveis são os valores únicos presentes na coluna "Canal de Vendas" do DataFrame.

Filtragem dos Dados:

    df_filtered = df1[df1["Data Emissão Pedido"] == month]:
        Filtra o DataFrame df1 para selecionar apenas as linhas onde a coluna "Data Emissão Pedido" corresponde ao mês selecionado.
        O DataFrame filtrado é armazenado em df_filtered.

Visualização de Dados:

Gráfico de Pizza:

    fig_kind = px.pie(df_filtered, values="Valor", names="Produto", title="Analise de Vendas "):
        Cria um gráfico de pizza utilizando a biblioteca plotly.express.
        O gráfico exibe a distribuição do "Valor" por "Produto" no DataFrame filtrado.
        O título do gráfico é "Analise de Vendas".
    col4.plotly_chart(fig_kind, use_container_width=True):
        Exibe o gráfico de pizza na quarta coluna da interface Streamlit.
        O gráfico ocupa toda a largura disponível da coluna.

Tabela de Dados Filtrados:

    st.write(df_filtered):
        Exibe o DataFrame filtrado df_filtered na interface Streamlit.

Gráfico de Barras por Dia:

    fig_date = px.bar(df_filtered, x="Data Emissão Pedido", y="Canal de Vendas", color="Valor", title="Pedido"):
        Cria um gráfico de barras utilizando a biblioteca plotly.express.
        O gráfico exibe a distribuição do "Valor" por "Data Emissão Pedido" e "Canal de Vendas" no DataFrame filtrado.
        A cor das barras representa o "Valor".
        O título do gráfico é "Pedido".
    col1.plotly_chart(fig_date, use_container_width=True):
        Exibe o gráfico de barras na primeira coluna da interface Streamlit.
