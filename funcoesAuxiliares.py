from time import sleep
import sys
import pyautogui
import constantesTextos
import constantesPosicoes

def esperar():
    sleep(1)

def clicar(posicao):
    esperar()
    pyautogui.click(posicao)

def escrever(texto):
    esperar()
    pyautogui.write(texto)

def apertar(botao):
    esperar()
    pyautogui.press(botao)

def rolar(rolagem):
    esperar()
    pyautogui.scroll(rolagem)

def exportarDados():
    pyautogui.rightClick(constantesPosicoes.PONTO_REF_TABELA) # Clicar com o botão direito na tabela.
    sleep(2)
    # pyautogui.doubleClick(x=1569, y=430) # Clicar na opção table
    clicar(constantesPosicoes.POSICAO_ITEM_TABELA) # Clicar na opção table
    sleep(2)
    apertar('tab')
    sleep(2)
    apertar('down', presses=6)
    sleep(2)
    apertar('enter') # Clicar na opção Download as.
    sleep(2)
    clicar(constantesPosicoes.POSICAO_ITEM_DADOS) # Clicar na opção Data.
    sleep(2)
    clicar(constantesPosicoes.POSICAO_EXPORTAR) # Clicar na opção Export.
    sleep(2)
    clicar(constantesPosicoes.POSICAO_LINK) # Clicar no Link Azul de Download.
    sleep(5)
    apertar('tab') # Clica no Close
    sleep(2)
    apertar('enter')
    sleep(2)

def escolherPorUF():
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_POR_UF)
    esperar()

def escolherPorCNPJ():
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_POR_CNPJ)
    esperar()

def selecionarMacros():
    macro = int(input("Digite 1 para escolher a macro PorUF ou digite 2 para escolher a macro PorCNPJ: "))

    print('Selecionando ano')
    print("0 - 2020\n1 - 2021\n2 - 2022\n3 - 2023\n4 - 2024\n5 - 2025")
    ano = int(input("Selecione um número de 0 a 5 para escolher um ano para filtragem: "))

    if macro == 1:
        escolherPorUF()
    elif macro == 2:
        escolherPorCNPJ()
    else:
        sys.exit("Número da macro inválido.")

    if not 0 <= ano <= 5:
        sys.exit("Número de ano inválido.")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_ANO)
    escrever(constantesTextos.ANO[ano])
    apertar('enter')
    apertar('esc')

# -- Funções de carregamento --

def carregarBolsaFamilia():
    print('Carregando filtro - Bolsa Familia')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    clicar(constantesPosicoes.POSICAO_BF_NAO)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_BF_NAO)
    clicar(constantesPosicoes.POSICAO_BF_SIM)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_BF_SIM)
    esperar()

def carregarSituacaoDePobreza():
    print('Carregando filtro - Situação de Pobreza')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)
    clicar(constantesPosicoes.POSICAO_SP_NAO)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SP_NAO)
    clicar(constantesPosicoes.POSICAO_SP_SIM)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SP_SIM)
    esperar()

def carregarSetorEconomico():
    print('Carregando filtro - Setor Economico')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_AGR)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SE_AGR)
    clicar(constantesPosicoes.POSICAO_SE_CMR)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SE_CMR)
    clicar(constantesPosicoes.POSICAO_SE_CST)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SE_CST)
    clicar(constantesPosicoes.POSICAO_SE_IND)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SE_IND)
    clicar(constantesPosicoes.POSICAO_SE_SER)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SE_SER)
    esperar()
    
def carregarUF():
    pass

def carregarMunicipio():
    pass

def carregarSexo():
    print('Carregando filtro - Sexo')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)
    clicar(constantesPosicoes.POSICAO_SX_HOM)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SX_HOM)
    clicar(constantesPosicoes.POSICAO_SX_MUL)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SX_MUL)
    clicar(constantesPosicoes.POSICAO_SX_NID)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_SX_NID)
    esperar()

def carregarRaçaCor():
    print('Carregando filtro - Raça/Cor')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_AMA)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_CR_AMA)
    clicar(constantesPosicoes.POSICAO_CR_BRC)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_CR_BRC)
    clicar(constantesPosicoes.POSICAO_CR_IND)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_CR_IND)
    clicar(constantesPosicoes.POSICAO_CR_NID)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_CR_NID)
    clicar(constantesPosicoes.POSICAO_CR_NIN)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_CR_NIN)
    clicar(constantesPosicoes.POSICAO_CR_PRD)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_CR_PRD)
    clicar(constantesPosicoes.POSICAO_CR_PRT)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_CR_PRT)
    esperar()

def carregarGrauDeInstrucao():
    print('Carregando filtro - Grau de Instrução')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_1)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_1)
    clicar(constantesPosicoes.POSICAO_GI_2)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_2)
    clicar(constantesPosicoes.POSICAO_GI_3)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_3)
    clicar(constantesPosicoes.POSICAO_GI_4)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_4)
    clicar(constantesPosicoes.POSICAO_GI_5)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_5)
    clicar(constantesPosicoes.POSICAO_GI_6)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_6)
    clicar(constantesPosicoes.POSICAO_GI_7)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_7)
    clicar(constantesPosicoes.POSICAO_GI_8)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_8)

    rolar(-200) # Scroll antes da posição 9

    clicar(constantesPosicoes.POSICAO_GI_9)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_9)
    clicar(constantesPosicoes.POSICAO_GI_10)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_10)
    clicar(constantesPosicoes.POSICAO_GI_11)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_11)
    clicar(constantesPosicoes.POSICAO_GI_12)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_12)
    clicar(constantesPosicoes.POSICAO_GI_13)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_GI_13)
    esperar() 

def carregarFaixaEtaria():
    print('Carregando filtro - Faixa Etária')
    clicar(constantesPosicoes.PONTO_REF)
    
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)

    clicar(constantesPosicoes.POSICAO_FE_18A24)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_18A24)
    clicar(constantesPosicoes.POSICAO_FE_25A29)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_25A29)
    clicar(constantesPosicoes.POSICAO_FE_30A39)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_30A39)
    clicar(constantesPosicoes.POSICAO_FE_40A49)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_40A49)
    clicar(constantesPosicoes.POSICAO_FE_50A59)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_50A59)
    clicar(constantesPosicoes.POSICAO_FE_60A64)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_60A64)
    clicar(constantesPosicoes.POSICAO_FE_ACI65)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_ACI65)
    clicar(constantesPosicoes.POSICAO_FE_ATE17)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_ATE17)

    rolar(-200) #scroll 

    clicar(constantesPosicoes.POSICAO_FE_DTNMV)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_DTNMV)
    clicar(constantesPosicoes.POSICAO_FE_DNULL)
    sleep(5)
    clicar(constantesPosicoes.POSICAO_FE_DNULL)
    esperar()

def carregarFiltros():
    carregarBolsaFamilia()
    carregarSituacaoDePobreza()
    carregarSetorEconomico()
    carregarSexo()
    carregarRaçaCor()
    carregarGrauDeInstrucao()
    carregarFaixaEtaria()
