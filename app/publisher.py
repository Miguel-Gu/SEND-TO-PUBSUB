import os
import json
from google.cloud import pubsub_v1
from fastapi.logger import logger


PROJECT_ID = os.getenv("PROJECT_ID")
TOPIC = os.getenv("PROJECT_ID")

publisher_data = pubsub_v1.PublisherClient()


def publish_data(data):
    try:
        future = publisher_data.publish(
            f"projects/{PROJECT_ID}/topics/{TOPIC}", json.dumps(data).encode('utf-8')
        )
        logger.info(f"O dado está sendo enviado para {TOPIC}")
        message_id = future.result()
        logger.info(f"Dado enviado para o pubsub: {message_id}")

    except Exception as error:
        logger.exception(f"Falha ao enviar o dado para o tópico {TOPIC}")
        logger.exception(str(error))
