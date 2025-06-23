FROM python:3.12.9-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

# Install system dependencies including git
RUN apt-get update && apt-get install -y git && apt-get clean

# Install Python packages
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8050

CMD ["python", "app.py"]