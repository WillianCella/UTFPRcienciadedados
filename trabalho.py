import imp
import streamlit as st
import pandas as pd


votacao_2022 =  pd.read_csv("./data/votacao_secao_2022_PR.csv",sep=";", encoding='latin1' )

st.title("Super trabalho eleitoral")

st.write("""
# Base das eleições presidenciais 2022
"""
)

# Define um DF com os votos por Estados
estados = votacao_2022['SG_UF'].unique()
estado = st.sidebar.selectbox('Selecione o Estado', estados)
votos_UF = votacao_2022[votacao_2022['SG_UF'] == estado]

# Cria um dicionário com o código do cargo e a descrição do cargo
cargos_dict = votos_UF[['CD_CARGO', 'DS_CARGO']].set_index('CD_CARGO').to_dict()
cargos_dict = cargos_dict['DS_CARGO']
cargo = st.sidebar.selectbox('Selecione o cargo', sorted(list(cargos_dict.values())))

# Cria um DF com os votos dos candidatos do Estado por cargo
votos_cargo = votos_UF[votos_UF['DS_CARGO'] == cargo]

# Cria um dicionário com o número e nome dos candidatos pelo cargo selecionado
candidatos_dict = votos_cargo[['NR_VOTAVEL', 'NM_VOTAVEL']].set_index('NR_VOTAVEL').to_dict(orient='dict')
candidatos_dict = candidatos_dict['NM_VOTAVEL']
candidato = st.sidebar.selectbox('Selecione o candidato', sorted(list(candidatos_dict.values())))

frame = pd.DataFrame(sorted(list(candidatos_dict.items())),columns = ['Número votável', 'Nome candidato'])
st.dataframe(frame)

# Seleciona o candidato
cod_candidato = 0
for codigo, candidato_ in candidatos_dict.items():
    if candidato_ == candidato:
        cod_candidato = codigo
st.write(f'Candidato {candidato}, número: {cod_candidato}')

# Define um DF com os votos por município
municipios = sorted(votos_UF['NM_MUNICIPIO'].unique())
municipio = st.selectbox('Selecione um município', municipios)
votos_municipio = votos_UF[votos_UF['NM_MUNICIPIO'] == municipio]

st.write(f'O município "{municipio}" gerou {len(votos_municipio)} votos')

# Apresenta a quantidade de votos que o candidato conseguiu no município
votos_candidato_municipio = votos_municipio[votos_municipio['NR_VOTAVEL'] == cod_candidato]
st.write(f'O candidato "{candidato} - {cod_candidato}" conseguiu {len(votos_candidato_municipio)} em {municipio}')
