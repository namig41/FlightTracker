FROM python:3.10

RUN mkdir /booking

WORKDIR /booking

COPY req.txt .

RUN pip install -r req.txt

COPY . .

CMD ["uvicorn",  "app.main:app", "--reload"]
