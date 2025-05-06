from time import sleep
import pandas as pd
from funcoesAuxiliares import carregarFiltros, selecionarMacros

# ---- FUNCAO PRINCIPAL ----

def main():
    print('Inicializando script')
    macro, ano = selecionarMacros()
    carregarFiltros(macro, ano)
    print('Extração finalizada')

if __name__ == '__main__':
    main()