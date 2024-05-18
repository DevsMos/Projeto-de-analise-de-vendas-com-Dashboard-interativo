import streamlit as st 
import pandas as pd
import plotly.express as px
import openpyxl



st.set_page_config("WIDE")

df1 = pd.read_excel("Plan_vendas.xlsx",
                 sheet_name="Plan",
                 usecols="A:K",
                 header=0)

# Converter a coluna "Date" para o formato de data
df1["Data Emissão Pedido"] = pd.to_datetime(df1["Data Emissão Pedido"])
df1 = df1.sort_values("Data Emissão Pedido")




# Criar uma nova coluna "Month" que contém o ano e o mês
df1["Data Emissão Pedido"] = df1["Data Emissão Pedido"].apply(lambda x: str(x.year) + "-" + str(x.month))
print (df1)
col1,col2,col3  = st.columns(3) # Primeira linha com duas colunas
col5,col4,col6 = st.columns(3) # Segunda linha com três colunas

#*******************************************************************************************************************************
month = st.sidebar.selectbox("Selecione Produto", df1["Produto"].unique())
prod = st.sidebar.selectbox("Selecione o Estado",df1["Estado"].unique())
cliente = st.sidebar.selectbox("Selecione Cliente",df1["Canal de Vendas"].unique())

#*******************************************************************************************************************************



# Filtrar os dados com base no mês selecionado
df_filtered = df1[df1["Data Emissão Pedido"] == month]

# Criar o gráfico de pizza para exibir o faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Produto", names="Valor",
                   title="Analise de Vendas ")

# Exibir o gráfico na quarta coluna
col4.plotly_chart(fig_kind, use_container_width=True)

# Criar uma nova coluna "Month" que contém o ano e o mês

df_filtered = df1[df1["Produto"] == month]

# Exibir o DataFrame filtrado
st.write(df_filtered)

col1,col2,  = st.columns(2) # Primeira linha com duas colunas
col3,col4, = st.columns(2) # Segunda linha com três colunas
col5 = st.columns(1) # Segunda linha com três colunas

# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Data Emissão Pedido", y="Canal de Vendas", color="Valor", title="Pedido")

# Exibir o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)
#---------------------------------------------------------------------------------------------------------------------------#

# Criar o gráfico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Data Emissão Pedido", y="Canal de Vendas", 
                  color="Estado", title="Vendas Estado",
                  orientation="h")

# Exibir o gráfico na segunda coluna
col2.plotly_chart(fig_prod, use_container_width=True)

#---------------------------------------------------------------------------------------------------------------------------#

# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Canal de Vendas", y="Valor", color="Data Emissão Pedido", title="Vendas por Empresa")

# Exibir o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)
