# Use a imagem oficial do Python 3.13 slim
FROM python:3.13-slim

# Variáveis de ambiente para Python e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VIRTUALENVS_CREATE=false

# Instalando dependências de sistema (mínimo necessário para build)
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalando Poetry (versão >= 2.0 para compatibilidade com pyproject.toml)
RUN pip install "poetry>=2.0.0"

# Definindo diretório de trabalho
WORKDIR /app

# Copiando arquivos de dependências
COPY pyproject.toml poetry.lock ./

# Instalando dependências do projeto
# --no-root evita instalar o código fonte neste passo para otimizar o cache
RUN poetry install --only main --no-root

# Copiando o restante do código fonte do projeto
COPY . .

# Instalando o projeto em si (registra o pacote 'tax_simulator' no Python)
RUN poetry install --only main

# Expondo a porta padrão do Streamlit
EXPOSE 8501

# Variáveis de ambiente para o Streamlit rodar corretamente no container
ENV STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Comando para iniciar o aplicativo Streamlit
CMD ["streamlit", "run", "app/main.py"]
