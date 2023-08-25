import streamlit as st
import re
import requests

def validar_cpf(cpf):
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return False
    return True

def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def buscar_cidades(estado):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"
    response = requests.get(url)
    cidades = [cidade["nome"] for cidade in response.json()]
    return cidades

def main():
    st.title("Formulário de Cadastro e Venda")

    nome = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")

    if not validar_cpf(cpf):
        st.warning("CPF inválido. Use o formato 000.000.000-00")
        return

    cpf_formatado = formatar_cpf(cpf)

    idade = st.number_input("Idade", min_value=0, max_value=150, step=1)
    salario = st.number_input("Salário", min_value=0.0)
    
    profissoes_comuns = [
        "Engenheiro", "Médico", "Advogado", "Professor", "Empresário",
        "Analista de Sistemas", "Arquiteto", "Dentista", "Enfermeiro",
        "Psicólogo", "Administrador", "Veterinário", "Farmacêutico",
        "Designer", "Nutricionista", "Outra"
    ]
    
    
    profissao = st.selectbox("Profissão", profissoes_comuns)

    if profissao == "Outra":
        profissao = st.text_input("Qual a sua profissão?")
        
    estado = st.selectbox("Estado", [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    ])
    
    cidades = buscar_cidades(estado)
    cidade = st.selectbox("Cidade", cidades)
    
    linha = st.selectbox("Linha", ["Vida", "Previdência"])

    if linha == "Vida":
        produtos = ["Vida_01", "Vida_02"]
    elif linha == "Previdência":
        produtos = ["Prev_01", "Prev_02"]
    else:
        produtos = []

    produto_selecionado = st.selectbox("Produto", produtos)

    if st.button("Venda"):
        st.write("Dados enviados:")
        st.write(f"Nome: {nome}")
        st.write(f"CPF: {cpf_formatado}")
        st.write(f"Idade: {idade}")
        st.write(f"Salário: {salario}")
        st.write(f"Profissão: {profissao}")
        st.write(f"Estado: {estado}")
        st.write(f"Cidade: {cidade}")
        st.write(f"Linha: {linha}")
        st.write(f"Produto: {produto_selecionado}")

if __name__ == "__main__":
    main()
