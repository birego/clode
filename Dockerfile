# Utilisez une image Python officielle comme base
FROM python:3.8-alpine

COPY requirements.txt requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "view.py" ]