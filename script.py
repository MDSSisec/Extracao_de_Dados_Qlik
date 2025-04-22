# ---- IMPORTS ----

from time import sleep

# import keyboard
import pyautogui
import pandas as pd

# ---- CONSTANTES ----

MEIO_DA_TELA = (1064, 260)
POSICAO_DO_ANO = (178, 296)
POSICAO_DO_MES = (108, 340)
POSICAO_DO_CADUNICO = (159, 381)
POSICAO_DA_BOLSA_FAMILIA = (170, 420)
POSICAO_DA_SITUACAO_DE_POBREZA = (187, 457)
POSICAO_DO_SETOR_ECONOMICO = (177, 499)
POSICAO_DA_UF = (181, 537)
POSICAO_DO_MUNICIPIO = (151, 579)
POSICAO_DO_SEXO = (173, 618)
POSICAO_DA_RACA = (181, 660)
POSICAO_DO_GRAU_DE_INSTRUCAO = (176, 703)
POSICAO_DA_FAIXA_ETARIA = (197, 744)

# PASSO A PASSO DO SCRIPT
PASSO00 = '00 - SCRIPT INICIALIZADO:'
PASSO01 = '01 - BUSCANDO ANO'
PASSO02 = '02 - BUSCANDO MES'
PASSO03 = '03 - BUSCANDO CADUNICO'
PASSO04 = '04 - BUSCANDO BOLSA FAMILIA'
PASSO05 = '05 - BUSCANDO SITUACAO DE POBREZA'
PASSO06 = '06 - BUSCANDO SETOR ECONOMICO'
PASSO07 = '07 - BUSCANDO UF'
PASSO08 = '08 - BUSCANDO POR MUNICIPIO'
PASSO09 = '09 - BUSCANDO POR SEXO'
PASSO10 = '10 - BUSCANDO POR RACA'
PASSO11 = '11 - BUSCANDO POR GRAU DE INSTRUCAO'
PASSO12 = '12 - BUSCANDO POR FAIXA ETARIA'
PASSO13 = '13 - '
PASSO14 = '14 - '

# PASSO A PASSO DOWNLOAD
PASSOD00 = '00 - DOWNLOAD INICIALIZADO:'
PASSOD01 = '01 - ESCOLHENDO OPCAO DE DOWNLOAD'
PASSOD02 = '02 - ESCOLHENDO OPCAO DE EXPORTAR'
PASSOD03 = '03 - CLICANDO NO LINK AZUL DE DOWNLOAD'
PASSOD04 = '04 - FECHANDO A TELA DE DOWNLOAD'

UF = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
GRAU_DE_INSTRUCAO = ['5 completo fundamental', '6 a 9 fundamental', 'Analfabeto', 'Até 5 incompleto', 'Doutorado', 'Fundamental Completo', 'Médio Completo', 'Médio Incompleto', 'Mestrado', 'Pós-graduação Completa', 'Superior Completo', 'Superior Incompleto', 'Não Identificado']
FAIXA_ETARIA = ['18 a 24 anos', '25 a 29 anos', '30 a 39 anos', '40 a 49 anos', '50 a 59 anos', '60 a 64 anos', 'Acima dos 65 anos', 'Até 17 anos', 'Data de Nascimento Nula', 'Data de Nascimento igual ou maior que a data de movimentação']
MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
RACA = ['Amarela', 'Branca', 'Indígena','Não Identificado', "Não informado" ,'Parda', 'Preta']
SETOR_ECONOMICO = ['Agropecuária','Comércio' ,'Construção', 'Indústria', 'Serviços']
ANO = ['2020', '2021', '2022', '2023', '2024', '2025']
SITUACAO_DE_POBREZA = ['Sim', 'Não']
SEXO = ['Masculino', 'Feminino']
BOLSA_FAMILIA = ['Sim', 'Não'] # Lembrando q aqui vamos indicar qual indice da lista deve ser selecionado. (0 ou 1) (BOLSA_FAMILIA[0])
CADUNICO = ['Sim', 'Não']
MUNICIPIO = ['']

# ---- FUNCOES AUXILIARES ----

# A ideia seria chamar a função de exportar dados sempre ao final de cada passo.

def exportarDados():
    print(PASSOD00)
    pyautogui.rightClick(x=1544, y=417) # Clicar com o botão direito na tabela.
    sleep(2)
    # pyautogui.doubleClick(x=1569, y=430) # Clicar na opção table
    pyautogui.click(x=1569, y=430) # Clicar na opção table
    sleep(2)
    pyautogui.press('tab')
    sleep(2)
    pyautogui.press('down', presses=6)
    sleep(2)
    pyautogui.press('enter') # Clicar na opção Download as.
    sleep(2)
    print(PASSOD02)
    pyautogui.click(x=1611, y=514) # Clicar na opção Data.
    sleep(2)
    print(PASSOD03)
    pyautogui.click(x=1097, y=654) # Clicar na opção Export.
    sleep(2)
    print(PASSOD04)
    pyautogui.click(x=863, y=591) # Clicar no Link Azul de Download.
    sleep(5)
    pyautogui.press('tab') # Clica no Close
    sleep(2)
    pyautogui.press('enter')
    sleep(2)

def escolherAno():
    sleep(1)
    pyautogui.click(MEIO_DA_TELA)
    sleep(1)
    pyautogui.click(POSICAO_DO_ANO)
    sleep(1)
    pyautogui.write(ANO[5])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')
    sleep(2)
    exportarDados()

def escolherMes():  
    pyautogui.click(MEIO_DA_TELA)
    sleep(1)
    pyautogui.click(POSICAO_DO_MES)
    sleep(1)
    pyautogui.write(MESES[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherCadunico():
    pyautogui.click(MEIO_DA_TELA)
    sleep(1)
    pyautogui.click(POSICAO_DO_CADUNICO)
    sleep(1)
    pyautogui.write(CADUNICO[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherBolsaFamilia():
    pyautogui.click(MEIO_DA_TELA)
    sleep(1)
    pyautogui.click(POSICAO_DA_BOLSA_FAMILIA)
    sleep(1)
    pyautogui.write(BOLSA_FAMILIA[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

def escolherSituacaoDePobreza():
    pyautogui.click(MEIO_DA_TELA)
    sleep(1)
    pyautogui.click(POSICAO_DA_SITUACAO_DE_POBREZA)
    sleep(1)
    pyautogui.write(SITUACAO_DE_POBREZA[0])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('esc')

# ---- FUNCAO PRINCIPAL ----

def main():
    # print(PASSO00)
    print(PASSO02)
    escolherMes()
    sleep(1)
    # print(PASSO01)
    escolherAno()
    sleep(1)
    # sleep(1)
    # print(PASSO03)
    # escolherCadunico()
    # sleep(1)
    # print(PASSO04)
    # escolherBolsaFamilia()
    # sleep(1)
    # print(PASSO05)
    # escolherSituacaoDePobreza()
    # sleep(1)
    # print(PASSO06)
    # escolherSetorEconomico()


if __name__ == '__main__':
    main()



