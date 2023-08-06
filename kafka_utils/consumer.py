from json import loads
from typing import TypedDict
from kafka import KafkaConsumer as _KafkaConsumer

from logging_config import setup_logging
from .settings import (
    KAFKA_TOPIC,
    KAFKA_CONSUMER_LOGNAME,
    KAFKA_CONSUMER_LOGFILE,
    KAFKA_BOOTSTRAP_SERVERS,
)

logging = setup_logging(
    KAFKA_CONSUMER_LOGNAME,
    KAFKA_CONSUMER_LOGFILE,
)


class ResultType(TypedDict):
    website_url: str
    status_code: int
    response_time: float
    pattern_found: bool | None


class KafkaConsumer:

    def __init__(self) -> None:
        self.consumer = None

    def __enter__(self) -> _KafkaConsumer:
        consumer_config = {
            'enable_auto_commit': True,
            'auto_offset_reset': 'earliest',
            'bootstrap_servers': KAFKA_BOOTSTRAP_SERVERS,
            'value_deserializer': lambda value: loads(value.decode('utf-8')),
        }
        try:
            self.consumer = _KafkaConsumer(KAFKA_TOPIC, **consumer_config)
            logging.info("Kafka consumer started.")
            return self.consumer
        except Exception as e:
            logging.error(f"Error setting up Kafka consumer: {str(e)}")
            raise Exception("Error setting up Kafka consumer")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.consumer is not None:
            self.consumer.close()
            logging.info("Kafka consumer closed.")


def consume_from_kafka(*, consumer: _KafkaConsumer):
    try:
        for message in consumer:
            data = message.value
            logging.info(f"Received check result from Kafka: {data}")
            yield data
    except KeyboardInterrupt:
        logging.warning("Kafka consumer interrupted.")
