FROM python:3.10-slim
WORKDIR /app
COPY metadata.py, publisher_manager.py config.py, scripts.logs.py . .
RUN pip install -r requirements.txt
CMD ["python", "publisher_manager"]
