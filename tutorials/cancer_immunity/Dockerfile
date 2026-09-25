FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5050 \
    DATA_DIR=/data

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY content/ content/
COPY templates/ templates/
COPY static/ static/

VOLUME ["/data"]
EXPOSE 5050

CMD ["gunicorn", "--workers", "2", "--threads", "4", \
     "--bind", "0.0.0.0:5050", \
     "--access-logfile", "-", "--error-logfile", "-", \
     "app:app"]
