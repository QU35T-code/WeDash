FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /dashboard
COPY requirements.txt /dashboard/
RUN pip install -r requirements.txt
COPY . /dashboard/
