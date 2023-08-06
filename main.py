from website import check_website
from logging_config import setup_logging
from database import (
    create_table,
    store_to_database
)
from kafka_utils import (
    KafkaProducer,
    send_to_kafka,
    KafkaConsumer,
    consume_from_kafka,
)


def main() -> None:

    WEBSITES = [
        'http://google.com',
        "https://www.iranserver.com/",
    ]

    with KafkaProducer() as producer:

        for site in WEBSITES:
            result = check_website(site)

            if result:
                try:
                    send_to_kafka(
                        result=result,
                        producer=producer,
                    )
                except:
                    continue

    with KafkaConsumer() as consumer:
        for data in consume_from_kafka(consumer=consumer):
            store_to_database(**data)


if __name__ == "__main__":
    create_table()
    main()
