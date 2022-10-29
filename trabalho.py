import streamlit as st
import pandas as pd
import numpy as np


votacao_2022 =  pd.read_csv("./data/votacao_secao_2022_PR.csv",sep=";", encoding='latin1' )

st.title("Super trabalho eleitoral")

st.write("""
# Base das eleições presidenciais 2022
"""
)



# Cria um dicionário com o código do cargo e a descrição do cargo
cargos = votacao_2022[['CD_CARGO', 'DS_CARGO']].set_index('CD_CARGO').to_dict()
cargos = cargos['DS_CARGO']
cargos

# Seleciona o código do cargo
cod_cargo_candidato = 3
cargo_candidato = cargos.get(cod_cargo_candidato)
cargo_candidato

# Define um dataframe dos votos com os candidatos do cargo selecionado
votos_cargo = votacao_2022[votacao_2022['CD_CARGO'] == cod_cargo_candidato]

# Cria um dicionário com o número e nome dos candidatos pelo cargo selecionado
candidatos = votos_cargo[['NR_VOTAVEL', 'NM_VOTAVEL']].set_index('NR_VOTAVEL').to_dict(orient='dict')
candidatos = candidatos['NM_VOTAVEL']

frame = pd.DataFrame(list(candidatos.items()),columns = ['Número votável', 'Nome candidato'])
st.dataframe(frame)

# # Cria um dicionário com o código do cargo e a descrição do cargo
# cargos = votacao_2022[['CD_CARGO', 'DS_CARGO']].set_index('CD_CARGO').to_dict()
# cargos = cargos['DS_CARGO']
# cargos

# ### Estados 
# estados = data_detran['uf'].unique()
# estado = st.selectbox("Estados", estados)
# base_estados = data_detran[data_detran['uf'] == estado] 

# municipios = base_estados['municipio'].unique()
# municipio = st.multiselect("Estados", municipios)
# base_municipio = base_estados[base_estados['municipio'].isin(municipio)]

# result = pd.crosstab(base_municipio['municipio'], base_municipio['br'])

