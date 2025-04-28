from time import sleep
import pyautogui
import pandas as pd
import constantesPosicoes

# toDo:
#       - modularizar funcoes em arquivo separado
#       - substituir funcoes de click individual em filtros pelas funçoes de carregamento:
#           * funcao escolherBolsaFamilia ira virar carregarBF que sera responsavel por carregar o filtro bolsa familia sim/nao
#           * as funcoes de carregamento individual serao chamadas em sequencia na funcao carregarDados()

# -- Arrays com os itens dos filtros -- 
# - Os itens serão buscados através do índice no array. Ex: UF[1] = "Acre" -
# - Os itens dos arrays devem ser normalizados removendo caracteres especiais em geral -

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
    pyautogui.rightClick(constantesPosicoes.PONTO_REF_TABELA) # Clicar com o botão direito na tabela.
    sleep(2)
    # pyautogui.doubleClick(x=1569, y=430) # Clicar na opção table
    pyautogui.click(constantesPosicoes.POSICAO_ITEM_TABELA) # Clicar na opção table
    sleep(2)
    pyautogui.press('tab')
    sleep(2)
    pyautogui.press('down', presses=6)
    sleep(2)
    pyautogui.press('enter') # Clicar na opção Download as.
    sleep(2)
    print(PASSOD02)
    pyautogui.click(constantesPosicoes.POSICAO_ITEM_DADOS) # Clicar na opção Data.
    sleep(2)
    print(PASSOD03)
    pyautogui.click(constantesPosicoes.POSICAO_EXPORTAR) # Clicar na opção Export.
    sleep(2)
    print(PASSOD04)
    pyautogui.click(constantesPosicoes.POSICAO_LINK) # Clicar no Link Azul de Download.
    sleep(5)
    pyautogui.press('tab') # Clica no Close
    sleep(2)
    pyautogui.press('enter')
    sleep(2)

def escolherPorUF():
    sleep(1)
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_POR_UF)
    sleep(1)

def escolherPorCNPJ():
    sleep(1)
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_POR_CNPJ)
    sleep(1)

def escolherAno():
    sleep(1)
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DO_ANO)
    sleep(1)
    pyautogui.write(ANO[1])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')
    sleep(1)

def escolherMes():  
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DO_MES)
    sleep(1)
    pyautogui.write(MESES[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherCadunico():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DO_CADUNICO)
    sleep(1)
    pyautogui.write(CADUNICO[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherBolsaFamilia():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    sleep(1)
    pyautogui.write(BOLSA_FAMILIA[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherSituacaoDePobreza():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)
    sleep(1)
    pyautogui.write(SITUACAO_DE_POBREZA[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherSetorEconomico():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    sleep(1)
    pyautogui.write(SETOR_ECONOMICO[4]) #, interval=0.10
    # sleep(0.5)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherUF():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_DA_UF)
    sleep(1)
    pyautogui.write(UF[0])

    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherMunicipio(): # não vai ser utilizado por agora
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DO_MUNICIPIO)
    sleep(1)
    pyautogui.write(MUNICIPIO[0]) 
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherSexo():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DO_SEXO)
    sleep(1)
    pyautogui.write(SEXO[0])
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherRaçaCor():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DA_RACA)
    sleep(1)
    pyautogui.write(RACA[0])
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherGrauDeInstrucao():  # vai ser necessário utilizar navegacao por tabulacao aqui por conta de que não existem palavras exclusivas para cada filtro
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    sleep(1)
    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('down', presses=5) # cada press é para cada item de GRAU_DE_INSTRUCAO
    sleep(1)
    pyautogui.press('space') 
    sleep(1)
    pyautogui.press('enter')

def escolherFaixaEtaria():
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    sleep(1)
    pyautogui.write(FAIXA_ETARIA[0])
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def carregarDados():
    print("carregarDados()")
    pyautogui.click(constantesPosicoes.PONTO_REF)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_BF_NAO)
    sleep(3)

    pyautogui.click(constantesPosicoes.POSICAO_BF_NAO)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_BF_SIM)
    sleep(3)

    pyautogui.click(constantesPosicoes.POSICAO_BF_SIM)
    sleep(1)
    pyautogui.click(constantesPosicoes.PONTO_REF)

# ---- FUNCAO PRINCIPAL ----

def main():
    print('Inicializando script')
    escolherPorUF()
    escolherAno()
    carregarDados()

if __name__ == '__main__':
    main()