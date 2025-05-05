from time import sleep
import os
import sys
import pyautogui
import constantesTextos
import constantesPosicoes
from datetime import datetime

# === VARIÁVEIS GLOBAIS ===
PASTA_DOWNLOADS = r"D:\Donwloads\QLIK"
macro_atual = None
ano_atual = None

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

def get_ultimo_arquivo_baixado():
    arquivos = [os.path.join(PASTA_DOWNLOADS, f)
                for f in os.listdir(PASTA_DOWNLOADS)
                if f.endswith(".xlsx")]
    if not arquivos:
        raise FileNotFoundError("Nenhum arquivo .xlsx encontrado na pasta de downloads.")
    return max(arquivos, key=os.path.getmtime)

def renomear_ultimo_download(macro, ano, filtro_tag, filtro_pasta):
    novo_nome = f"{macro}_{ano}_{filtro_tag}.xlsx"

    pasta_base = os.path.join(PASTA_DOWNLOADS, macro, str(ano))
    if filtro_pasta:
        pasta_destino = os.path.join(pasta_base, filtro_pasta)
    else:
        pasta_destino = pasta_base

    os.makedirs(pasta_destino, exist_ok=True)

    caminho_destino = os.path.join(pasta_destino, novo_nome)

    if os.path.exists(caminho_destino):
        raise FileExistsError(f"O arquivo {caminho_destino} já existe. Abortando.")

    sleep(2.5)  # alterar aqui?
    arquivo_origem = get_ultimo_arquivo_baixado()
    os.rename(arquivo_origem, caminho_destino)
    print(f"✅ Arquivo movido para: {caminho_destino}")

def exportarDados(macro, ano, filtro_tag, filtro_pasta=None):
    clicarDireito(constantesPosicoes.PONTO_REF_TABELA, 2)
    clicar(constantesPosicoes.POSICAO_ITEM_TABELA)
    clicar(constantesPosicoes.POSICAO_ITEM_BAIXAR)
    clicar(constantesPosicoes.POSICAO_ITEM_DADOS)
    clicar(constantesPosicoes.POSICAO_ITEM_EXPORTAR)
    clicar(constantesPosicoes.POSICAO_ITEM_LINK)
    clicar(constantesPosicoes.POSICAO_ITEM_FECHAR)
    pausaCurta()
    sleep(12) # ou alterar aqui
    renomear_ultimo_download(macro, ano, filtro_tag, filtro_pasta)

# === INTERAÇÃO ===

def selecionarMacros():
    macro_opcao = int(input("Digite 1 para escolher a macro PorUF ou digite 2 para escolher a macro PorCNPJ: "))
    ano_opcao = int(input("Selecione um número de 0 a 5 para escolher o ano (0=2020, 1=2021, ..., 5=2025): "))

    macro = "PorUF" if macro_opcao == 1 else "PorCNPJ"
    ano = 2020 + ano_opcao

    if macro_opcao not in [1, 2]:
        sys.exit("Número da macro inválido.")
    if not 0 <= ano_opcao <= 5:
        sys.exit("Número de ano inválido.")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_ANO)
    escrever(str(ano))
    apertar('enter')
    apertar('esc')

    sleep(3)

    exportarDados(macro, ano, "GERAL", None)

    return macro, ano 

def carregarBolsaFamilia(macro, ano):
    print('Carregando filtro - Bolsa Familia')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)

    clicar(constantesPosicoes.POSICAO_BF_NAO)
    pausaLonga()
    exportarDados(macro, ano, "PBF_NAO", "BolsaFamilia")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    clicar(constantesPosicoes.POSICAO_BF_NAO)
    clicar(constantesPosicoes.POSICAO_BF_SIM)
    pausaLonga()
    exportarDados(macro, ano, "PBF_SIM", "BolsaFamilia")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_BOLSA_FAMILIA)
    clicar(constantesPosicoes.POSICAO_BF_ANC)
    pausaCurta()

def carregarSituacaoDePobreza(macro, ano):
    print('Carregando filtro - Situação de Pobreza')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)

    clicar(constantesPosicoes.POSICAO_SP_NAO)
    pausaLonga()
    exportarDados(macro, ano, "SP_NAO", "SituacaoPobreza")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)
    clicar(constantesPosicoes.POSICAO_SP_NAO)
    clicar(constantesPosicoes.POSICAO_SP_SIM)
    pausaLonga()
    exportarDados(macro, ano, "SP_SIM", "SituacaoPobreza")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_SITUACAO_DE_POBREZA)
    clicar(constantesPosicoes.POSICAO_SP_ANC)
    pausaCurta()

def carregarSetorEconomico(macro, ano):
    print('Carregando filtro - Setor Economico')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)

    clicar(constantesPosicoes.POSICAO_SE_AGR)
    pausaLonga()
    exportarDados(macro, ano, "SE_AGR", "SetorEconomico")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_CMR)
    pausaLonga()
    exportarDados(macro, ano, "SE_CMR", "SetorEconomico")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_CST)
    pausaLonga()
    exportarDados(macro, ano, "SE_CST", "SetorEconomico")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_IND)
    pausaLonga()
    exportarDados(macro, ano, "SE_IND", "SetorEconomico")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    clicar(constantesPosicoes.POSICAO_SE_SER)
    pausaLonga()
    exportarDados(macro, ano, "SE_SER", "SetorEconomico")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SETOR_ECONOMICO)
    clicar(constantesPosicoes.POSICAO_SE_ANC)
    pausaCurta()
    
def carregarUF():
    pass

def carregarMunicipio():
    pass

def carregarSexo(macro, ano):
    print('Carregando filtro - Sexo')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)

    clicar(constantesPosicoes.POSICAO_SX_HOM)
    pausaLonga()
    exportarDados(macro, ano, "SX_HOM", "Sexo")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)
    clicar(constantesPosicoes.POSICAO_SX_ANC)
    clicar(constantesPosicoes.POSICAO_SX_MUL)
    pausaLonga()
    exportarDados(macro, ano, "SX_MUL", "Sexo")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)
    clicar(constantesPosicoes.POSICAO_SX_ANC)
    clicar(constantesPosicoes.POSICAO_SX_NID)
    pausaLonga()
    exportarDados(macro, ano, "SX_NID", "Sexo")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_SEXO)
    clicar(constantesPosicoes.POSICAO_SX_ANC)
    pausaCurta()

def carregarRacaCor(macro, ano):
    print('Carregando filtro - Raça/Cor')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)

    clicar(constantesPosicoes.POSICAO_CR_AMA)
    pausaLonga()
    exportarDados(macro, ano, "CR_AMA", "RacaCor")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_BRC)
    pausaLonga()
    exportarDados(macro, ano, "CR_BRC", "RacaCor")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_IND)
    pausaLonga()
    exportarDados(macro, ano, "CR_IND", "RacaCor")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_NID)
    pausaLonga()
    exportarDados(macro, ano, "CR_NID", "RacaCor")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_NIN)
    pausaLonga()
    exportarDados(macro, ano, "CR_NIN", "RacaCor")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_PRD)
    pausaLonga()
    exportarDados(macro, ano, "CR_PRD", "RacaCor")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    clicar(constantesPosicoes.POSICAO_CR_PRT)
    pausaCurta()
    exportarDados(macro, ano, "CR_PRT", "RacaCor")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_RACA)
    clicar(constantesPosicoes.POSICAO_CR_ANC)
    pausaCurta()

def carregarGrauDeInstrucao(macro, ano):
    print('Carregando filtro - Grau de Instrução')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)

    for i in range(1, 14):
        if i > 8:
            rolar(-200)
        clicar(constantesPosicoes.POSICAO_GI_ANC)
        clicar(getattr(constantesPosicoes, f"POSICAO_GI_{i}"))
        pausaLonga()
        exportarDados(macro, ano, f"GI_{i}", "GrauInstrucao")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DO_GRAU_DE_INSTRUCAO)
    clicar(constantesPosicoes.POSICAO_GI_ANC)
    pausaCurta()

def carregarFaixaEtaria(macro, ano):
    print('Carregando filtro - Faixa Etária')
    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)

    faixas = [
        ("FE_18A24", constantesPosicoes.POSICAO_FE_18A24),
        ("FE_25A29", constantesPosicoes.POSICAO_FE_25A29),
        ("FE_30A39", constantesPosicoes.POSICAO_FE_30A39),
        ("FE_40A49", constantesPosicoes.POSICAO_FE_40A49),
        ("FE_50A59", constantesPosicoes.POSICAO_FE_50A59),
        ("FE_60A64", constantesPosicoes.POSICAO_FE_60A64),
        ("FE_ACI65", constantesPosicoes.POSICAO_FE_ACI65),
        ("FE_ATE17", constantesPosicoes.POSICAO_FE_ATE17),
        ("FE_DTNMV", constantesPosicoes.POSICAO_FE_DTNMV),
        ("FE_DNULL", constantesPosicoes.POSICAO_FE_DNULL),
    ]

    for tag, pos in faixas:
        clicar(constantesPosicoes.PONTO_REF)
        clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
        clicar(constantesPosicoes.POSICAO_FE_ANC)
        if tag in ["FE_DTNMV", "FE_DNULL"]:
            rolar(-200)
        clicar(pos)
        pausaLonga()
        exportarDados(macro, ano, tag, "FaixaEtaria")

    clicar(constantesPosicoes.PONTO_REF)
    clicar(constantesPosicoes.POSICAO_DA_FAIXA_ETARIA)
    clicar(constantesPosicoes.POSICAO_FE_ANC)
    pausaCurta()

def carregarFiltros(macro, ano):
    carregarBolsaFamilia(macro, ano)
    carregarSituacaoDePobreza(macro, ano)
    carregarSetorEconomico(macro, ano)
    carregarSexo(macro, ano)
    carregarRacaCor(macro, ano)
    carregarGrauDeInstrucao(macro, ano)
    carregarFaixaEtaria(macro, ano)

