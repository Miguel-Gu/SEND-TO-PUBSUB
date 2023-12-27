# SEND-TO-PUBSUB

Modelo de API em Cloud [Run](https://cloud.google.com/run?hl=pt-BR) para enviar dados de um modelo de usuário para um tópico [Pub/Sub](https://cloud.google.com/pubsub/docs/overview?hl=pt-br), com uma assinatura de envio para o BigQuery.


## Linguagem
Essa aplicação utiliza como linguagem o [Python 3.9](https://www.python.org/).


### Configuração prévia
Inicialmente, será necessário um tópico Pub/Sub em funcionamento, com uma [assinatura](https://cloud.google.com/pubsub/docs/bigquery?hl=pt-br) do BigQuery configurada, para que posteriormente sejam geradas as visões em cima do dado raw.


Com o tópico configurado, altere a linha 11 e 12 do Dockerfile, colocando as informações corretas do PROJECT_ID e do TOPIC que foi criado.


### Build e Run do Container

Antes de subir o container, é necessário que você configure a autenticação do GCP dentro do seu container. Para saber como, clique [aqui](https://cloud.google.com/run/docs/testing/local?hl=pt-br#docker-with-google-cloud-access).


Para buildar uma imagem Docker e em seguida subir um Container, execute os seguintes comandos:


1. docker build -t sendtopubsub .
2. docker run -d --name sendtopubsub -p 80:80 sendtopubsub


Com isso, você terá uma imagem Docker em funcionamento:


<p align="center">
<img src="https://uploaddeimagens.com.br/images/004/691/366/original/containerfuncionando.png">
</p>


E ao acessar o endpoint "/docs", verá a seguinte página:


<p align="center">
<img src="https://uploaddeimagens.com.br/images/004/691/368/original/printdoswagger.png">
</p>