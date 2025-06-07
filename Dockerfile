FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY bot.py .

# Use polling by default; override CMD in Koyeb if using webhooks
CMD ["python", "bot.py"]
