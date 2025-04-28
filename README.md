# Script de Extração de Dados Qlik

Este é um script Python desenvolvido para automatizar a extração de dados do Qlik Sense. O script utiliza a biblioteca PyAutoGUI para simular interações com a interface do usuário, permitindo a extração automatizada de dados com diferentes filtros.

## 🚫 Repositório Privado

Este é um repositório privado e não aceita colaborações externas.

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- PyAutoGUI
- Pandas

## 📋 Funcionalidades

O script permite a extração de dados com os seguintes filtros:
- Ano (2020-2025)
- Mês
- CadÚnico (Sim/Não)
- Bolsa Família (Sim/Não)
- Situação de Pobreza (Sim/Não)
- Setor Econômico
- UF
- Município
- Sexo
- Raça
- Grau de Instrução
- Faixa Etária

## 📁 Estrutura do Projeto

- `arquivoPrincipal.py`: Arquivo principal que contém a função main e coordena a execução do script
- `constantesPosicoes.py`: Contém as constantes de posições de tela para interação com a interface
- `constantesTextos.py`: Contém as constantes de textos utilizados nos filtros (anos, meses, UFs, etc.)
- `funcoesAuxiliares.py`: Contém as funções auxiliares para manipulação dos filtros
- `scriptCapturaPosicao.py`: Script auxiliar para capturar posições de tela
- `requirements.txt`: Lista de dependências do projeto

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone https://github.com/MDSSisec/Extracao_de_Dados_Qlik.git
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

1. Certifique-se de que o Qlik Sense está aberto e na visualização correta
2. Execute o script principal:
```bash
python arquivoPrincipal.py
```

## ⚠️ Importante

- O script utiliza coordenadas de tela específicas, portanto, é necessário ajustar as coordenadas caso a resolução ou o layout da tela seja diferente

- Esta automação só funcionará corretamente se o navegador estiver em tela cheia e a resolução da tela principal for 1920x1080.

- Certifique-se de não mover o mouse durante a execução do script

- O script inclui pausas (sleep) para garantir que as ações sejam executadas corretamente

## 🔧 Ferramentas Auxiliares

- `scriptCapturaPosicao.py`: Utilize este script para capturar novas posições de tela quando necessário
