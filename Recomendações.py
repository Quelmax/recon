import streamlit as st
import pandas as pd
import datarules as rules
import time

df= pd.read_csv('data/modelo_recomendação.csv')

df1 = rules.getCrossSell(df)
df2 = rules.getUpSell(df)
nomes_filtrados = ['Enrico Oliveira']
df3 = df[df['nome'].isin(nomes_filtrados)]

def listProducts(row):
    col_produtos = [col for col in row.index if 'produto' in col.lower()]
    produtos = [col for col in col_produtos if pd.notnull(row[col])]
    return row[produtos]

def maisPrev(row):
    if pd.isnull(row['of_previdencia']):
        return "No momento esse cliente não possui recomendação"
    else:
        return row['of_previdencia']
    
def compara(row, col1, col2):
    valor_col1 = row[col1]
    valor_col2 = row[col2]
    
    if valor_col1 == valor_col2:
        return valor_col1.upper()
    else:
        return f"1. {valor_col1} \n2. {valor_col2} :star:"
    

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
                st.subheader("Produtos recomendados:", help="Analisando sua carteira com nosso modelo de recomendação inteligente vimos que esse produto pode ser de interesse do seu cliente")
                res = row['crossell'].upper()
                st.write(res)


      

with tab2:
    st.write("Esses clientes da sua carteira podem realizar um upgrade em produtos que já possuem:")
    # st.write(df2)
    for index, row in df2.iterrows():
        row_expander = st.expander(f" {index} - {row['nome']}", False)
        
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
                st.subheader("Produto recomendado:",help="Analisando sua carteira com nosso modelo de recomendação inteligente vimos que esse produto pode ser de interesse do seu cliente. Produto com estrela significa maior rentabilidade para você!")
                # res = row['upsell'].upper()
                # st.write(res)
                st.write(compara(row, 'upsell', 'upsell_maiorcomissao' ) )
                st.subheader("Mais Previdência", help="Esse cliente tem boas chances de adquirir também esse produto de previdência")
                st.write(maisPrev(row))
                
               

with tab3:
    st.write("Esses clientes estão com indicativo de possível saída, que tal entrar em contato com eles?")
    # st.write(df3)

    for index, row in df3.iterrows():

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
                st.subheader("Ponto de Atenção:")
                st.write('O Sr. Enrico Oliveira tem seguro de vida há 30 meses. De acordo com nosso modelo inteligente, ele pode cancelar o contrato (possibilidade de churn de 75%). Você pode entrar em contato, dar um atendimento especial, saber o que ele quer e evitar o cancelamento.')
                st.subheader("Assistente Icatu")
                with st.spinner('Estou pensando...'):
                    time.sleep(3)
                st.success('Pronto!')
                st.write("Sou o **Icatúlio**, assistente virtual da Icatu Seguros, venho trazer uma sugestão de abordagem para o cliente Enrico Oliveira:")
                st.write("Olá, Sr. Enrico. Aqui é o seu corretor de seguros da Icatu. Estou ligando para saber como você está e se você está satisfeito com o seu seguro de vida. Você sabe que o seu seguro é muito importante para garantir a sua tranquilidade e a de sua família, não é mesmo? Você tem seguro de vida há 30 meses e isso mostra que você se preocupa com o seu futuro. Mas eu gostaria de conversar com você sobre algumas vantagens que você pode ter ao continuar com a nossa seguradora. Você sabia que você pode ter descontos progressivos, coberturas adicionais e benefícios exclusivos? Você conhece todas as opções de planos e serviços que nós oferecemos? Você tem alguma dúvida ou sugestão? Eu estou aqui para te ouvir e te ajudar no que for preciso. Eu quero oferecer um atendimento especial para você, pois você é um cliente muito valioso para nós. Por favor, me diga o que você precisa e o que eu posso fazer para te atender melhor. Eu tenho certeza que podemos encontrar uma solução que atenda às suas expectativas e necessidades.")
                