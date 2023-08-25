import streamlit as st
import openai

openai.api_type = "azure"
openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.api_base = "https://openia-datathon-time04.openai.azure.com/"
openai.api_version = "2023-03-15-preview"

    
st.title("💬 Icatu Chat") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Me chamo Icatúlio, seu assitente de recomendações Icatu, como posso te ajudar?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    print(msg)


if prompt := st.chat_input():
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(deployment_id="icatu-gpt-35-turbo", model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)


with st.expander("Sugestões de frase"):
    st.write("""
        Elabore um pitch de venda do seguro [NOME DO SEGURO] para o cliente de nome [NOME DO CLIENTE], ciente de que ele possui as seguintes características: [CASADO, SE TEM FILHOS, PROFISSÃO...].
    """) 