FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libmagic1 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN pip install uv && uv sync

COPY . .

CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "8000"]