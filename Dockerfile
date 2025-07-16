FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Pass the commit SHA in at runtime. This is a placeholder; it will be overridden by Kubernetes.
ENV COMMIT_SHA=""

CMD ["python", "app.py"]