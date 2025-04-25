from time import sleep
import pyautogui
import pandas as pd

# toDo: 
#       - Normalizar itens do array de Grau de Instrução, deixando apenas uma palavra exclusiva de cada item.
#       - Criar funções para selcionar PorUf e PorCNPJ
#       - Criar menu para passagem de parametros (PorUF ou PorCNPJ e Qual ano) 

# ---- CONSTANTES DE POSIÇÃO GERAL ----
PONTO_REF = (200, 100)
POSICAO_POR_UF = (600, 250)
POSICAO_POR_CNPJ = (1300 , 250)
POSICAO_DO_ANO = (200, 150)
POSICAO_DO_MES = (200, 200)
POSICAO_DO_CADUNICO = (200, 250)
POSICAO_DA_BOLSA_FAMILIA = (200, 300)
POSICAO_DA_SITUACAO_DE_POBREZA = (200, 350)
POSICAO_DO_SETOR_ECONOMICO = (200, 400)
POSICAO_DA_UF = (200, 455)
POSICAO_DO_MUNICIPIO = (200, 520) 
POSICAO_DO_SEXO = (200, 560) 
POSICAO_DA_RACA = (200, 620)
POSICAO_DO_GRAU_DE_INSTRUCAO = (200, 670)
POSICAO_DA_FAIXA_ETARIA = (200, 720)

# --- CONSTANTES DE DOWNLOAD ----
PONTO_REF_TABELA    = (1300, 400)
POSICAO_ITEM_TABELA = (1305, 405)
POSICAO_ITEM_BAIXAR = (1305, 600)
POSICAO_ITEM_DADOS  = (1305, 500)
POSICAO_EXPORTAR    = (1100, 600)
POSICAO_LINK        = (900,  550)


# Constantes indicando a etapa do script
PASSO00 = '00 - SCRIPT INICIALIZADO:'
PASSOPORUF = 'SELECIONANDO POR UF'
PASSOPORCNPJ = 'SELECIONANDO POR CNPJ'
PASSO01 = '01 - SELECIONANDO ANO'
PASSO02 = '02 - SELECIONANDO MES'
PASSO03 = '03 - SELECIONANDO CADUNICO'
PASSO04 = '04 - SELECIONANDO BOLSA FAMILIA'
PASSO05 = '05 - SELECIONANDO SITUACAO DE POBREZA'
PASSO06 = '06 - SELECIONANDO SETOR ECONOMICO'
PASSO07 = '07 - SELECIONANDO UF'
PASSO08 = '08 - SELECIONANDO MUNICIPIO'
PASSO09 = '09 - SELECIONANDO SEXO'
PASSO10 = '10 - SELECIONANDO RACA'
PASSO11 = '11 - SELECIONANDO GRAU DE INSTRUCAO'
PASSO12 = '12 - SELECIONANDO FAIXA ETARIA'
PASSO13 = '13 - '
PASSO14 = '14 - '

# PASSO A PASSO DOWNLOAD
PASSOD00 = '00 - DOWNLOAD INICIALIZADO:'
PASSOD01 = '01 - ESCOLHENDO OPCAO DE DOWNLOAD'
PASSOD02 = '02 - ESCOLHENDO OPCAO DE EXPORTAR'
PASSOD03 = '03 - CLICANDO NO LINK AZUL DE DOWNLOAD'
PASSOD04 = '04 - FECHANDO A TELA DE DOWNLOAD'


# -- Arrays com os itens dos filtros --
# -- Os itens serão buscados através do índice no array. Ex: UF[1] = "Acre" --
# -- Os itens dos arrays devem ser normalizados removendo caracteres especiais em geral --

ANO = [
    '2020', '2021', '2022', 
    '2023', '2024', '2025'
]

MESES = [
    'janeiro', 'fevereiro', 'marco', 
    'abril', 'maio', 'junho', 
    'julho', 'agosto', 'setembro', 
    'outubro', 'novembro', 'dezembro'
]

CADUNICO = ['Sim', 'Nao']

BOLSA_FAMILIA = ['Sim', 'Nao']

SITUACAO_DE_POBREZA = ['Sim', 'Nao']

SETOR_ECONOMICO = [
    'Agropecuaria', 'Comercio', 'Construcao', 
    'Industria', 'Servicos'
]

UF = [
    'Acre', 'Alagoas', 'Amapa', 
    'Amazonas', 'Bahia', 'Ceara', 
    'Distrito Federal', 'Espirito Santo', 
    'Goias', 'Maranhao', 'Mato Grosso', 
    'Mato Grosso do Sul', 'Minas Gerais', 
    'Para', 'Paraiba', 'Parana', 
    'Pernambuco', 'Piaui', 'Rio de Janeiro', 
    'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondonia',
    'Roraima', 'Santa Catarina', 'Sao Paulo', 
    'Sergipe', 'Tocantins'
]

MUNICIPIO = ['']

SEXO = ['Homem', 'Mulher', 'Nao Identificado']

RACA = [
    'Amarela', 'Branca', 'Indigena',
    'Nao Identificado', 'Nao informado', 'Parda', 
    'Preta'
]

GRAU_DE_INSTRUCAO = [
    "5º completo fundamental", "6ª a 9ª fundamental", "Analfabeto",
    "Até 5º incompleto", "Doutorado", "Fundamental completo",
    "Médio completo", "Médio incompleto", "Mestrado",
    "Não identificado", "Pós-graduação completa", "Superior completo",
    "Superior incompleto"
]


FAIXA_ETARIA = [
    '18', '25', '30', 
    '40', '50', '60', 
    'Acima dos 65 anos', 'Ate 17 anos', 'Nula', 
    'movimentacao'
]

# ---- FUNCOES AUXILIARES ----

# A ideia seria chamar a função de exportar dados sempre ao final de cada passo.

def esperar():
    sleep(1)

def exportarDados():
    print(PASSOD00)
    pyautogui.rightClick(PONTO_REF_TABELA) # Clicar com o botão direito na tabela.
    sleep(2)
    # pyautogui.doubleClick(x=1569, y=430) # Clicar na opção table
    pyautogui.click(POSICAO_ITEM_TABELA) # Clicar na opção table
    sleep(2)
    pyautogui.press('tab')
    sleep(2)
    pyautogui.press('down', presses=6)
    sleep(2)
    pyautogui.press('enter') # Clicar na opção Download as.
    sleep(2)
    print(PASSOD02)
    pyautogui.click(POSICAO_ITEM_DADOS) # Clicar na opção Data.
    sleep(2)
    print(PASSOD03)
    pyautogui.click(POSICAO_EXPORTAR) # Clicar na opção Export.
    sleep(2)
    print(PASSOD04)
    pyautogui.click(POSICAO_LINK) # Clicar no Link Azul de Download.
    sleep(5)
    pyautogui.press('tab') # Clica no Close
    sleep(2)
    pyautogui.press('enter')
    sleep(2)

def escolherPorUF():
    sleep(1)
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_POR_UF)

def escolherPorCNPJ():
    sleep(1)
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_POR_CNPJ)

def escolherAno():
    sleep(1)
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DO_ANO)
    sleep(1)
    pyautogui.write(ANO[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherMes():  
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DO_MES)
    sleep(1)
    pyautogui.write(MESES[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherCadunico():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DO_CADUNICO)
    sleep(1)
    pyautogui.write(CADUNICO[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherBolsaFamilia():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DA_BOLSA_FAMILIA)
    sleep(1)
    pyautogui.write(BOLSA_FAMILIA[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherSituacaoDePobreza():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DA_SITUACAO_DE_POBREZA)
    sleep(1)
    pyautogui.write(SITUACAO_DE_POBREZA[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherSetorEconomico():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DO_SETOR_ECONOMICO)
    sleep(1)
    pyautogui.write(SETOR_ECONOMICO[4]) #, interval=0.10
    # sleep(0.5)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherUF():
    pyautogui.click(PONTO_REF)
    sleep(1)

    pyautogui.click(POSICAO_DA_UF)
    sleep(1)
    pyautogui.write(UF[0])

    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherMunicipio(): # não vai ser utilizado por agora
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DO_MUNICIPIO)
    sleep(1)
    pyautogui.write(MUNICIPIO[0]) 
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherSexo():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DO_SEXO)
    sleep(1)
    pyautogui.write(SEXO[0])
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherRaçaCor():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DA_RACA)
    sleep(1)
    pyautogui.write(RACA[0])
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherGrauDeInstrucao():  # vai ser necessário utilizar navegacao por tabulacao aqui por conta de que não existem palavras exclusivas para cada filtro
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DO_GRAU_DE_INSTRUCAO)
    sleep(1)
    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('down', presses=5) # cada press é para cada item de GRAU_DE_INSTRUCAO
    sleep(1)
    pyautogui.press('space') 
    sleep(1)
    pyautogui.press('enter')

def escolherFaixaEtaria():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click(POSICAO_DA_FAIXA_ETARIA)
    sleep(1)
    pyautogui.write(FAIXA_ETARIA[0])
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

# funcao template para escolha dos filtros
def escolherTemplate():
    pyautogui.click(PONTO_REF)
    sleep(1)
    pyautogui.click('POSICAO')
    sleep(1)
    pyautogui.write('[0]')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

# ---- FUNCAO PRINCIPAL ----

def main():
    print(PASSO00)
    sleep(1)  # sleep para começar o script

    print(PASSOPORCNPJ)
    escolherPorCNPJ()
    sleep(1)

    print(PASSOPORUF)
    escolherPorUF()
    sleep(1)

    print(PASSO01)
    escolherAno()
    sleep(1)

    print(PASSO02)
    escolherMes()
    sleep(1)

    print(PASSO03)
    escolherCadunico()
    sleep(1)

    print(PASSO04)
    escolherBolsaFamilia()
    sleep(1)

    print(PASSO05)
    escolherSituacaoDePobreza()
    sleep(1)

    print(PASSO06)
    escolherSetorEconomico()
    sleep(1)

    print(PASSO07)
    escolherUF()
    sleep(1)

    print(PASSO09)
    escolherSexo()
    sleep(1)

    print(PASSO10)
    escolherRaçaCor()
    sleep(1)

    print(PASSO11)
    escolherGrauDeInstrucao()
    sleep(1)

    print(PASSO12)
    escolherFaixaEtaria()
    sleep(1)

    exportarDados()

if __name__ == '__main__':
    main()