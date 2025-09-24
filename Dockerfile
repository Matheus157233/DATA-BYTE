# Usa Python 3.11
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto para o container
COPY . /app

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta padrão do Streamlit
EXPOSE 7860

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "pa.py", "--server.port=7860", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]
