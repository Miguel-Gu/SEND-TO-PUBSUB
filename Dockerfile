FROM python:3.9

WORKDIR /SENDTOPUBSUB

COPY ./requirements.txt /SENDTOPUBSUB/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /SENDTOPUBSUB/requirements.txt

COPY ./app /SENDTOPUBSUB/app

ENV PROJECT_ID="seuprojeto"
ENV TOPIC="seutopico"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]