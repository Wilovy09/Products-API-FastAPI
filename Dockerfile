FROM python:3.11-slim

ENV PIP_DISAVLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]