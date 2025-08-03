# Dockerfile para construir a imagem de execução dos fluxos Prefect.
FROM prefecthq/prefect:2-python3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Comando padrão para iniciar um agente que escuta na fila 'kubernetes'
CMD ["prefect", "agent", "start", "-q", "kubernetes"]