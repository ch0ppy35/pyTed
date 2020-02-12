FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP pyTED.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers && apk add --update --no-cache gcc g++ gcc libxslt-dev musl-dev
RUN apk update && apk add postgresql-dev musl-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]