FROM python:3.10-slim
WORKDIR /app
COPY elastic.py, mongo.py, saver_manager.py, config.py, scripts.logs.py . .
RUN pip install -r requirements.txt
CMD ["python", "saver_manager"]
