import streamlit as st
import pandas as pd
import datarules as rules

df= pd.read_csv('data\modelo_recomendação.csv')

df1 = rules.getCrossSell(df)
df2 = rules.getUpSell(df)

def listProducts(row):
    col_produtos = [col for col in row.index if 'produto' in col.lower()]
    produtos = [col for col in col_produtos if pd.notnull(row[col])]
    return row[produtos]
    

# Layout das abas
tab1, tab2, tab3  = st.tabs(['Cross-Sell', 'Up-Sell', 'Retenção e Relacionamento'])

#nome, produto atual, comissão atual, produto recomendado, comissão

# Conteúdo das abas
with tab1:
    st.write("Esses clientes da sua carteira podem adquirir produtos de outra linha de négocio:")
    # st.write(df1)

    for index, row in df1.iterrows():

        row_expander = st.expander(f" {index} - {row['nome']}")
        
        with row_expander:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Informações do Cliente:')
                st.write("**Profissão**:", row['profissão'])
                st.write("**Idade**:", row['idade'])
                st.write("**Telefone :telephone:**:", row['telefone'])
                st.subheader('Produtos adquiridos:')
                st.dataframe(listProducts(row))


            with col2:
                st.subheader("Produto recomendado:")
                st.write(row['crossell'])

      

with tab2:
    st.write("Esses clientes da sua carteira podem realizar um upgrade em produtos que já possuem:")
    # st.write(df2)
    for index, row in df2.iterrows():
        row_expander = st.expander(f" {index} - {row['nome']}", False)
        
        with row_expander:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Informações do Cliente:')
                st.write("Profissão:", row['profissão'])
                st.write("Idade:", row['idade'])
                st.write("Telefone:", row['telefone'])
                st.subheader('Produtos adquiridos:')
                st.dataframe(listProducts(row))


            with col2:
                st.subheader("Produto recomendado:")
                st.write(row['upsell'])

# with tab3:
#     st.write("Esses clientes estão com indicativo de possível saída, que tal entrar em contato com eles?")
#     st.write(df3)

