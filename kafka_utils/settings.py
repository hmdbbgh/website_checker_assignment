from decouple import config


KAFKA_TOPIC = config(
    'KAFKA_TOPIC',
    default='websites_availability'
)
KAFKA_BOOTSTRAP_SERVERS = config(
    'KAFKA_BOOTSTRAP_SERVERS',
    default='localhost:9092'
)

REQUEST_TIMEOUT_MS = config(
    'REQUEST_TIMEOUT_MS',
    default=30_000,
    cast=int
)

MAX_BLOCK_MS = config(
    'MAX_BLOCK_MS',
    default=60_000,
    cast=int
)

KAFKA_PRODUCER_LOGNAME = config(
    'KAFKA_PRODUCER_LOGNAME',
    default='kafka_producer'
)
KAFKA_PRODUCER_LOGFILE = config(
    'KAFKA_PRODUCER_LOGFILE',
    default='logs/kafka_producer.log'
)

KAFKA_CONSUMER_LOGNAME = config(
    'KAFKA_CONSUMER_LOGNAME',
    default='kafka_consumer'
)
KAFKA_CONSUMER_LOGFILE = config(
    'KAFKA_CONSUMER_LOGFILE',
    default='logs/kafka_consumer.log'
)
