import os
import pandas as pd

ANO = '2025'  # Alterar
BASE_DIR = f'PorUF/{ANO}'

# Mapeamento das regras
MAPEAMENTO = {
    'BolsaFamilia': {
        f'PorUF_{ANO}_PBF_SIM.xlsx': ('Bolsa Familia', 'TRUE'),
        f'PorUF_{ANO}_PBF_NAO.xlsx': ('Bolsa Familia', 'FALSE'),
    },
    'SituacaoPobreza': {
        f'PorUF_{ANO}_SP_SIM.xlsx': ('Situação de Pobreza', 'TRUE'),
        f'PorUF_{ANO}_SP_NAO.xlsx': ('Situação de Pobreza', 'FALSE'),
    },
    'SetorEconomico': {
        f'PorUF_{ANO}_SE_AGR.xlsx': ('Setor Econômico', 'Agronegocio'),
        f'PorUF_{ANO}_SE_CMR.xlsx': ('Setor Econômico', 'Comercio'),
        f'PorUF_{ANO}_SE_CST.xlsx': ('Setor Econômico', 'Construcao'),
        f'PorUF_{ANO}_SE_IND.xlsx': ('Setor Econômico', 'Industria'),
        f'PorUF_{ANO}_SE_SER.xlsx': ('Setor Econômico', 'Servico'),
    },
    'Sexo': {
        f'PorUF_{ANO}_SX_HOM.xlsx': ('Sexo', 'Homem'),
        f'PorUF_{ANO}_SX_MUL.xlsx': ('Sexo', 'Mulher'),
        f'PorUF_{ANO}_SX_NID.xlsx': ('Sexo', 'Nao Identificado'),
    },
    'RacaCor': {
        f'PorUF_{ANO}_CR_AMA.xlsx': ('Raça/Cor', 'Amarelo'),
        f'PorUF_{ANO}_CR_BRC.xlsx': ('Raça/Cor', 'Branco'),
        f'PorUF_{ANO}_CR_IND.xlsx': ('Raça/Cor', 'Indigena'),
        f'PorUF_{ANO}_CR_NID.xlsx': ('Raça/Cor', 'Nao Identificado'),
        f'PorUF_{ANO}_CR_NIN.xlsx': ('Raça/Cor', 'Nao Informado'),
        f'PorUF_{ANO}_CR_PRD.xlsx': ('Raça/Cor', 'Pardo'),
        f'PorUF_{ANO}_CR_PRT.xlsx': ('Raça/Cor', 'Preto'),
    },
    'GrauInstrucao': {
        f'PorUF_{ANO}_GI_1.xlsx': ('Grau de Instrução', '5º completo fundamental'),
        f'PorUF_{ANO}_GI_2.xlsx': ('Grau de Instrução', '6º a 9º fundamental'),
        f'PorUF_{ANO}_GI_3.xlsx': ('Grau de Instrução', 'Analfabeto'),
        f'PorUF_{ANO}_GI_4.xlsx': ('Grau de Instrução', 'Até 5º incompleto'),
        f'PorUF_{ANO}_GI_5.xlsx': ('Grau de Instrução', 'Doutorado'),
        f'PorUF_{ANO}_GI_6.xlsx': ('Grau de Instrução', 'Fundamental completo'),
        f'PorUF_{ANO}_GI_7.xlsx': ('Grau de Instrução', 'Médio completo'),
        f'PorUF_{ANO}_GI_8.xlsx': ('Grau de Instrução', 'Médio incompleto'),
        f'PorUF_{ANO}_GI_9.xlsx': ('Grau de Instrução', 'Mestrado'),
        f'PorUF_{ANO}_GI_10.xlsx': ('Grau de Instrução', 'Pós-graduação completa'),
        f'PorUF_{ANO}_GI_11.xlsx': ('Grau de Instrução', 'Superior completo'),
        f'PorUF_{ANO}_GI_12.xlsx': ('Grau de Instrução', 'Superior incompleto'),
        f'PorUF_{ANO}_GI_13.xlsx': ('Grau de Instrução', 'Não identificado'),
    },
    'FaixaEtaria': {
        f'PorUF_{ANO}_FE_18A24.xlsx': ('Faixa Etária', '18 a 24 anos'),
        f'PorUF_{ANO}_FE_25A29.xlsx': ('Faixa Etária', '25 a 29 anos'),
        f'PorUF_{ANO}_FE_30A39.xlsx': ('Faixa Etária', '30 a 39 anos'),
        f'PorUF_{ANO}_FE_40A49.xlsx': ('Faixa Etária', '40 a 49 anos'),
        f'PorUF_{ANO}_FE_50A59.xlsx': ('Faixa Etária', '50 a 59 anos'),
        f'PorUF_{ANO}_FE_60A64.xlsx': ('Faixa Etária', '60 a 64 anos'),
        f'PorUF_{ANO}_FE_ACI65.xlsx': ('Faixa Etária', 'Acima de 65 anos'),
        f'PorUF_{ANO}_FE_ATE17.xlsx': ('Faixa Etária', 'Até 17 anos'),
        f'PorUF_{ANO}_FE_DNULL.xlsx': ('Faixa Etária', 'Data de nascimento nula'),
        f'PorUF_{ANO}_FE_DTNMV.xlsx': ('Faixa Etária', 'Data de nascimento inválida'),
    }
}

for pasta, arquivos in MAPEAMENTO.items():
    pasta_path = os.path.join(BASE_DIR, pasta)
    for arquivo, (coluna, valor) in arquivos.items():
        file_path = os.path.join(pasta_path, arquivo)
        if os.path.exists(file_path):
            print(f"Processando arquivo: {file_path}")
            df = pd.read_excel(file_path)
            df[coluna] = valor
            df.to_excel(file_path, index=False)
        else:
            print(f"⚠ Arquivo não encontrado: {file_path}")
