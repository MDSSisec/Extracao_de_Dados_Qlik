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

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
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
2. Execute o script:
```bash
python script.py
```

## ⚠️ Importante

- O script utiliza coordenadas de tela específicas, portanto, é necessário ajustar as coordenadas caso a resolução ou o layout da tela seja diferente
- Certifique-se de não mover o mouse durante a execução do script
- O script inclui pausas (sleep) para garantir que as ações sejam executadas corretamente

## 📝 Estrutura do Código

- `script.py`: Contém a lógica principal do script
- `requirements.txt`: Lista as dependências do projeto

## 🔒 Segurança

Este repositório é privado e contém informações sensíveis. Não compartilhe as credenciais ou dados de acesso. 