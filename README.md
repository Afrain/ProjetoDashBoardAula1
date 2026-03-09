# Projeto Dashboard - Estatistica Aplicada

Dashboard interativo desenvolvido com Python para analise de dados socioeconomicos.

## Tecnologias

- Python 3.10+
- Streamlit
- Pandas
- Matplotlib

## Estrutura do projeto

```text
ProjetoDashBoard/
|-- Dados.py
|-- Dashboard.py
|-- Graficos/
|   |-- criar_grafico_numero_filhos.py
|   |-- criar_grafico_salario.py
|   |-- grafico_estado_civil.py
|   `-- grafico_grau_de_instrucao.py
```

## O que o dashboard mostra

- Estado civil (grafico de pizza)
- Grau de instrucao (barra vertical)
- Numero de filhos (barra horizontal)
- Distribuicao de salarios (histograma)

## Como baixar e executar

### 1. Clonar o repositorio

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

### 2. Criar ambiente virtual (recomendado)

```bash
python -m venv .venv
```

### 3. Ativar ambiente virtual

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

CMD:

```cmd
.venv\Scripts\activate.bat
```

### 4. Instalar dependencias

```bash
pip install streamlit pandas matplotlib
```

Opcional: gerar `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Se o arquivo ja existir:

```bash
pip install -r requirements.txt
```

### 5. Executar o projeto

```bash
streamlit run Dashboard.py
```

Depois, abra no navegador a URL mostrada no terminal (normalmente `http://localhost:8501`).

## Erros comuns

- `streamlit` nao reconhecido:
  - Ative o ambiente virtual antes de executar.
- Arquivo nao encontrado ao rodar:
  - O arquivo principal e `Dashboard.py` (D maiusculo).
- Porta ocupada:
  - O Streamlit usa outra porta automaticamente (exemplo: 8502).

## Melhorias futuras

- Leitura de dados por CSV/Excel
- Filtros interativos no Streamlit
- Validacao automatica das colunas obrigatorias
