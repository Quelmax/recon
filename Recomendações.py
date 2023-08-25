import streamlit as st
import pandas as pd
import dbconnection as db


# Criar DataFrames de exemplo
data1 = {'Nome': ['Alice', 'Bob', 'Charlie'],
         'Idade': [25, 30, 22]}
db.getRecom()
df1 = pd.DataFrame(data1)


data2 = {'Cidade': ['Nova York', 'Los Angeles', 'Chicago'],
         'População': [8500000, 3900000, 2700000]}
df2 = pd.DataFrame(data2)

data3 = {'Produto': ['Maçã', 'Banana', 'Laranja'],
         'Preço': [1.0, 0.5, 0.75]}
df3 = pd.DataFrame(data3)


# Função para mostrar detalhes do pop-up
def show_popup(row):
    st.write(f"Detalhes da linha selecionada: {row}")

# Layout das abas
tab1, tab2, tab3  = st.tabs(['Cross-Sell', 'Up-Sell', 'Retenção e Relacionamento'])

#nome, produto atual, comissão atual, produto recomendado, comissão

# Conteúdo das abas
with tab1:
    st.write("Esses clientes da sua carteira podem adquirir produtos de outra linha de négocio:")
    # st.write(df1)
    for index, row in df1.iterrows():
        row_expander = st.expander(f" {index} - {row['Nome']}", False)
        
        with row_expander:
            st.write("Detalhes da linha:", index)
            st.write("Nome:", row['Nome'])
            st.write("Idade:", row['Idade'])
            # st.write("Cidade:", row['Cidade'])
    


with tab2:
    st.write("Esses clientes da sua carteira podem realizar um upgrade em produtos que já possuem:")
    st.write(df2)

with tab3:
    st.write("Esses clientes estão com indicativo de possível saída, que tal entrar em contato com eles?")
    st.write(df3)

