from json import dumps
from typing import TypedDict
from kafka import KafkaProducer as _KafkaProducer

from logging_config import setup_logging
from .settings import (
    KAFKA_TOPIC,
    MAX_BLOCK_MS,
    REQUEST_TIMEOUT_MS,
    KAFKA_PRODUCER_LOGNAME,
    KAFKA_PRODUCER_LOGFILE,
    KAFKA_BOOTSTRAP_SERVERS,
)

logging = setup_logging(
    KAFKA_PRODUCER_LOGNAME,
    KAFKA_PRODUCER_LOGFILE,
)


class ResultType(TypedDict):
    website_url: str
    status_code: int
    response_time: float
    pattern_found: bool | None


class KafkaProducer:

    def __init__(self) -> None:
        self.producer = None

    def __enter__(self) -> _KafkaProducer:
        producer_config = {
            'max_block_ms': MAX_BLOCK_MS,
            'request_timeout_ms': REQUEST_TIMEOUT_MS,
            'bootstrap_servers': KAFKA_BOOTSTRAP_SERVERS,
            'value_serializer': lambda value: dumps(value).encode('utf-8'),
        }
        try:
            self.producer = _KafkaProducer(**producer_config)
            logging.info("Kafka producer started.")
            return self.producer
        except Exception as e:
            logging.error(f"Error setting up Kafka producer: {str(e)}")
            raise Exception("Error setting up Kafka producer")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.producer is not None:
            self.producer.flush()
            self.producer.close()
            logging.info("Kafka producer closed.")


def send_to_kafka(
    *,
    producer: _KafkaProducer,
    result: ResultType
) -> None:
    try:
        producer.send(KAFKA_TOPIC, value=result)
        logging.info(f"Sent check result to Kafka: {result}")
    except Exception as e:
        logging.error(f"Error sending data to Kafka: {str(e)}")
