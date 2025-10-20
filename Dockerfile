# load base

# --- stage 1 ---
FROM python:3.11-slim as base

# create work directory
WORKDIR /app

# update/configure installs with apt-get
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# copy files to docker directory
COPY requirements.txt .

# run commands
RUN pip install --no-cache-dir -r requirements.txt

# -- stage 2 ---
FROM base as final

WORKDIR /app

COPY . .

RUN python app/train.py

# expose port
EXPOSE 8000

# run uvicorn/gunicorn 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
