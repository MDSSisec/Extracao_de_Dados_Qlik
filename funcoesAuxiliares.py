from time import sleep
import sys
import pyautogui
import constantesTextos
import constantesPosicoes

def esperar():
    sleep(1)

def exportarDados():
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
    pyautogui.click(constantesPosicoes.POSICAO_ITEM_DADOS) # Clicar na opção Data.
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_EXPORTAR) # Clicar na opção Export.
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_LINK) # Clicar no Link Azul de Download.
    sleep(5)
    pyautogui.press('tab') # Clica no Close
    sleep(2)
    pyautogui.press('enter')
    sleep(2)

def escolherPorUF():
    esperar()
    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_POR_UF)
    esperar()

def escolherPorCNPJ():
    esperar()
    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_POR_CNPJ)
    esperar()

def escolherMacro():
    macro = int(input("Digite 1 para escolher a macro PorUF ou digite 2 para escolher a macro PorCNPJ: "))
    if macro == 1:
        escolherPorUF()
        esperar()
    elif macro == 2:
        escolherPorCNPJ()
        esperar()
    else: sys.exit("Número Inválido")
        
def selecionarAno():
    print('Selecionando ano')
    print("0 - 2020")
    print("1 - 2021")
    print("2 - 2022")
    print("3 - 2023")
    print("4 - 2024")
    print("5 - 2025")
    ano = int(input("Selecione um número de 0 a 5 para escolher um ano para filtragem: "))
    
    if 0 <= ano <= 5:
        esperar()
        pyautogui.click(constantesPosicoes.PONTO_REF)
        esperar()
        pyautogui.click(constantesPosicoes.POSICAO_DO_ANO)
        esperar()
        pyautogui.write(constantesTextos.ANO[ano]) 
        esperar()
        pyautogui.press('enter')
        esperar()
        pyautogui.press('esc')
        esperar()
    else: sys.exit("Número Inválido")

def carregarBolsaFamilia():
    print('Carregando filtro - Bolsa Familia')
    esperar()
    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_BF_NAO)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_BF_NAO)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_BF_SIM)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_BF_SIM)
    esperar()

def carregarSituacaoDePobreza():
    print('Carregando filtro - Situação de Pobreza')
    esperar()
    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SP_NAO)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SP_NAO)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SP_SIM)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SP_SIM)
    esperar()

def carregarSetorEconomico():
    print('Carregando filtro - Setor Economico')
    esperar()
    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SE_AGR)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SE_AGR)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SE_CMR)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SE_CMR)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SE_CST)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SE_CST)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SE_IND)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SE_IND)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SE_SER)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SE_SER)
    esperar()
    
def carregarUF():
    pass

def carregarMunicipio():
    pass

def carregarSexo():
    print('Carregando filtro - Sexo')
    esperar()
    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_DO_SEXO)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SX_HOM)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SX_HOM)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SX_MUL)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SX_MUL)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_SX_NID)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_SX_NID)
    esperar()

def carregarRaçaCor():
    print('Carregando filtro - Raça/Cor')
    esperar()
    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_DA_RACA)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_CR_AMA)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_CR_AMA)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_CR_BRC)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_CR_BRC)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_CR_IND)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_CR_IND)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_CR_NID)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_CR_NID)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_CR_NIN)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_CR_NIN)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_CR_PRD)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_CR_PRD)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_CR_PRT)
    sleep(4)
    pyautogui.click(constantesPosicoes.POSICAO_CR_PRT)
    esperar()

def carregarGrauDeInstrucao():
    print('Carregando filtro - Grau de Instrução')
    esperar()

    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    
    pyautogui.click(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_1)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_1)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_2)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_2)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_3)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_3)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_4)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_4)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_5)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_5)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_6)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_6)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_7)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_7)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_8)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_8)
    sleep(1)

    # Scroll antes da posição 9
    pyautogui.scroll(-200)
    sleep(1)
    pyautogui.click(constantesPosicoes.POSICAO_GI_9)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_9)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_10)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_10)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_11)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_11)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_12)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_12)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_GI_13)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_GI_13)
    sleep(1) 

def carregarFaixaEtaria():
    print('Carregando filtro - Faixa Etária')
    esperar()

    pyautogui.click(constantesPosicoes.PONTO_REF)
    esperar()
    
    pyautogui.click(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_18A24)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_18A24)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_25A29)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_25A29)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_30A39)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_30A39)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_40A49)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_40A49)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_50A59)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_50A59)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_60A64)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_60A64)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_ACI65)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_ACI65)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_ATE17)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_ATE17)
    sleep(1)

    pyautogui.scroll(-200)
    esperar()
    pyautogui.click(constantesPosicoes.POSICAO_FE_DTNMV)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_DTNMV)
    sleep(1)

    pyautogui.click(constantesPosicoes.POSICAO_FE_DNULL)
    sleep(2)
    pyautogui.click(constantesPosicoes.POSICAO_FE_DNULL)
    sleep(1)

def carregarFiltros():
    # carregarBolsaFamilia()
    # carregarSituacaoDePobreza()
    # carregarSetorEconomico()
    # carregarSexo()
    # carregarRaçaCor()
    # carregarGrauDeInstrucao()
    carregarFaixaEtaria()
