from time import sleep
import pyautogui
import pandas as pd
from funcoesAuxiliares import carregarFiltros, selecionarMacros, exportarDados

# ---- FUNCAO PRINCIPAL ----

def main():
    print('Inicializando script')
    # selecionarMacros()    
    # selecionarAno()
    carregarFiltros()

if __name__ == '__main__':
    main()