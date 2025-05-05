from time import sleep
import sys
import pyautogui
import constantesTextos
import constantesPosicoes

# toDo: Adicionar lógica de exportação nos filtros restantes: GI, FE

def pausaCurta():
    sleep(1)

def pausaLonga():
    sleep(3.8)

def clicar(posicao):
    pausaCurta()
    pyautogui.click(posicao)

def clicarDireito(posicao, clicks=1):
    for _ in range(clicks):
        pausaCurta()
        pyautogui.rightClick(posicao)

def escrever(texto):
    pausaCurta()
    pyautogui.write(texto)

def apertar(botao, presses=1):
    pausaCurta()
    pyautogui.press(botao, presses=presses)

def rolar(rolagem):
    pausaCurta()
    pyautogui.scroll(rolagem)

def exportarDados():
    clicarDireito(constantesPosicoes.PONTO_REF_TABELA, 2) # Clicar com o botão direito na tabela.
    clicar(constantesPosicoes.POSICAO_ITEM_TABELA) # Clicar na opção table

    clicar(constantesPosicoes.POSICAO_ITEM_BAIXAR)
    # clicar(constantesPosicoes.POSICAO_ITEM_DADOS)
    # clicar(constantesPosicoes.POSICAO_ITEM_)

    # apertar('tab')
    # apertar('down', 6)
    # apertar('enter') # Clicar na opção Download as.
    clicar(constantesPosicoes.POSICAO_ITEM_DADOS) # Clicar na opção Data.
    clicar(constantesPosicoes.POSICAO_ITEM_EXPORTAR) # Clicar na opção Export.
    clicar(constantesPosicoes.POSICAO_ITEM_LINK) # Clicar no Link Azul de Download.
    clicar(constantesPosicoes.POSICAO_ITEM_FECHAR)
    pausaCurta()
    
def escolherPorUF():
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_POR_UF)
    pausaCurta()

def escolherPorCNPJ():
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_POR_CNPJ)
    pausaCurta()

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

    sleep(3)
    exportarDados()

# -- Funções de carregamento --

def carregarBolsaFamilia():
    print('Carregando filtro - Bolsa Familia')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)

    clicar(constantesPosicoes.POSICAO_BF_NAO)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    clicar(constantesPosicoes.POSICAO_BF_NAO)
    clicar(constantesPosicoes.POSICAO_BF_SIM)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    clicar(constantesPosicoes.POSICAO_BF_ANC) # na teoria iria ser SIM aqui, mas o fitro selecionado ocupa o primerio lugar da tabela
    pausaCurta()

def carregarSituacaoDePobreza():
    print('Carregando filtro - Situação de Pobreza')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)


    clicar(constantesPosicoes.POSICAO_SP_NAO)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)
    clicar(constantesPosicoes.POSICAO_SP_NAO)
    clicar(constantesPosicoes.POSICAO_SP_SIM)
    pausaLonga()
    exportarDados()


    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)
    clicar(constantesPosicoes.POSICAO_SP_ANC) # na teoria iria ser SIM aqui, mas o fitro selecionado ocupa o primerio lugar da tabela
    pausaCurta()

def carregarSetorEconomico():
    print('Carregando filtro - Setor Economico')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)

    clicar(constantesPosicoes.POSICAO_SE_AGR)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_CMR)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_CST)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_IND)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_SER)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    pausaCurta()
    
def carregarUF():
    pass

def carregarMunicipio():
    pass

def carregarSexo():
    print('Carregando filtro - Sexo')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)

    clicar(constantesPosicoes.POSICAO_SX_HOM)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)
    clicar(constantesPosicoes.POSICAO_SX_ANC)
    clicar(constantesPosicoes.POSICAO_SX_MUL)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)
    clicar(constantesPosicoes.POSICAO_SX_ANC)
    clicar(constantesPosicoes.POSICAO_SX_NID)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)
    clicar(constantesPosicoes.POSICAO_SX_ANC)
    pausaCurta()

def carregarRaçaCor():
    print('Carregando filtro - Raça/Cor')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)

    clicar(constantesPosicoes.POSICAO_CR_AMA)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_BRC)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_IND)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_NID)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_NIN)
    pausaLonga()
    exportarDados()


    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_PRD)
    pausaLonga()
    exportarDados()
    
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_PRT)
    pausaCurta()
    exportarDados()

def carregarGrauDeInstrucao():
    print('Carregando filtro - Grau de Instrução')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_1)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    clicar(constantesPosicoes.POSICAO_GI_2)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    clicar(constantesPosicoes.POSICAO_GI_3)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    clicar(constantesPosicoes.POSICAO_GI_4)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    clicar(constantesPosicoes.POSICAO_GI_5)
    pausaLonga()
    exportarDados()
    
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    clicar(constantesPosicoes.POSICAO_GI_6)
    pausaLonga()
    exportarDados()
    
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    clicar(constantesPosicoes.POSICAO_GI_7)
    pausaLonga()
    exportarDados()
    
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    clicar(constantesPosicoes.POSICAO_GI_8)
    pausaLonga()
    exportarDados()
    
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    rolar(-200) # Scroll antes da posição 9
    clicar(constantesPosicoes.POSICAO_GI_9)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    rolar(-200)
    clicar(constantesPosicoes.POSICAO_GI_10)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    rolar(-200)
    clicar(constantesPosicoes.POSICAO_GI_11)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    rolar(-200)
    clicar(constantesPosicoes.POSICAO_GI_12)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    rolar(-200)
    clicar(constantesPosicoes.POSICAO_GI_13)
    pausaLonga()
    exportarDados()

def carregarFaixaEtaria():
    print('Carregando filtro - Faixa Etária')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    clicar(constantesPosicoes.POSICAO_FE_18A24)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    clicar(constantesPosicoes.POSICAO_FE_ANC)
    clicar(constantesPosicoes.POSICAO_FE_25A29)
    pausaLonga()
    exportarDados()

    # clicar(constantesPosicoes.PONTO_REF)
    # clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    # clicar(constantesPosicoes.POSICAO_FE_ANC)
    # clicar(constantesPosicoes.POSICAO_FE_30A39)
    # pausaLonga()
    # exportarDados()

    # clicar(constantesPosicoes.PONTO_REF)
    # clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    # clicar(constantesPosicoes.POSICAO_FE_ANC)
    # clicar(constantesPosicoes.POSICAO_FE_40A49)
    # pausaLonga()
    # exportarDados()

    # clicar(constantesPosicoes.PONTO_REF)
    # clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    # clicar(constantesPosicoes.POSICAO_FE_ANC)
    # clicar(constantesPosicoes.POSICAO_FE_50A59)
    # pausaLonga()
    # exportarDados()

    # clicar(constantesPosicoes.PONTO_REF)
    # clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    # clicar(constantesPosicoes.POSICAO_FE_ANC)
    # clicar(constantesPosicoes.POSICAO_FE_60A64)
    # pausaLonga()
    # exportarDados()

    # clicar(constantesPosicoes.PONTO_REF)
    # clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    # clicar(constantesPosicoes.POSICAO_FE_ANC)
    # clicar(constantesPosicoes.POSICAO_FE_ACI65)
    # pausaLonga()
    # exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    clicar(constantesPosicoes.POSICAO_FE_ANC)
    clicar(constantesPosicoes.POSICAO_FE_ATE17)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    clicar(constantesPosicoes.POSICAO_FE_ANC)
    rolar(-200) # Scroll antes da posição 9
    clicar(constantesPosicoes.POSICAO_FE_DTNMV)
    pausaLonga()
    exportarDados()

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    clicar(constantesPosicoes.POSICAO_FE_ANC)
    rolar(-200) # Scroll antes da posição 9
    clicar(constantesPosicoes.POSICAO_FE_DNULL)
    pausaLonga()
    exportarDados()

def carregarFiltros():
    carregarBolsaFamilia()
    carregarSituacaoDePobreza()
    carregarSetorEconomico()
    carregarSexo()
    carregarRaçaCor()
    carregarGrauDeInstrucao()
    carregarFaixaEtaria()
