from time import sleep
import pyautogui
import pandas as pd
from funcoesAuxiliares import carregarFiltros, selecionarAno, escolherMacro

# toDo:
#       - modularizar funcoes em arquivo separado
#       - substituir funcoes de click individual em filtros pelas funçoes de carregamento:
#           * funcao escolherBolsaFamilia ira virar carregarBF que sera responsavel por carregar o filtro bolsa familia sim/nao
#           * as funcoes de carregamento individual serao chamadas em sequencia na funcao carregarDados()

# ---- FUNCAO PRINCIPAL ----

def main():
    print('Inicializando script')
    escolherMacro()    
    selecionarAno()
    carregarFiltros()

if __name__ == '__main__':
    main()