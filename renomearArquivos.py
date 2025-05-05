import os
import glob
from datetime import datetime

def renomear_arquivos_por_ordem(pasta):
    # Obtém o caminho absoluto da pasta
    pasta = os.path.abspath(pasta)
    
    # Verifica se a pasta existe
    if not os.path.exists(pasta):
        print(f"A pasta {pasta} não existe!")
        return
    
    # Lista todos os arquivos na pasta
    arquivos = glob.glob(os.path.join(pasta, '*'))
    
    # Filtra apenas arquivos (ignora pastas)
    arquivos = [f for f in arquivos if os.path.isfile(f)]
    
    # Ordena os arquivos por data de modificação
    arquivos.sort(key=lambda x: os.path.getmtime(x))
    
    # Renomeia os arquivos
    for i, arquivo in enumerate(arquivos, start=1):
        # Obtém a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1]
        
        # Cria o novo nome do arquivo
        novo_nome = os.path.join(pasta, f"{i:03d}{extensao}")
        
        # Renomeia o arquivo
        try:
            os.rename(arquivo, novo_nome)
            print(f"Renomeado: {os.path.basename(arquivo)} -> {os.path.basename(novo_nome)}")
        except Exception as e:
            print(f"Erro ao renomear {arquivo}: {str(e)}")

if __name__ == "__main__":
    pasta_alvo = "/home/administrador/Documentos/QLIK"
    print(f"Iniciando renomeação de arquivos em: {pasta_alvo}")
    renomear_arquivos_por_ordem(pasta_alvo)
    print("Processo concluído!") 